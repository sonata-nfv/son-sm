"""
Copyright (c) 2015 SONATA-NFV
ALL RIGHTS RESERVED.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Neither the name of the SONATA-NFV [, ANY ADDITIONAL AFFILIATION]
nor the names of its contributors may be used to endorse or promote
products derived from this software without specific prior written
permission.

This work has been performed in the framework of the SONATA project,
funded by the European Commission under Grant number 671517 through
the Horizon 2020 and 5G-PPP programmes. The authors would like to
acknowledge the contributions of their colleagues of the SONATA
partner consortium (www.sonata-nfv.eu).
"""
import logging
import yaml
import time
import threading
import os
import re
from sonmanobase import messaging


logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("son-sm-base")
LOG.setLevel(logging.DEBUG)
logging.getLogger("son-mano-base:messaging").setLevel(logging.INFO)


class sonSMbase(object):

    def __init__(self,
                 specific_manager_type = None,
                 service_name = None,
                 function_name = None,
                 specific_manager_name= None,
                 id_number = None,
                 update_version = 'false',
                 version= None,
                 description=None):
        """
        :param specific_manager_type: specifies the type of specific manager that could be either fsm or ssm.
        :param service_name: the name of the service that this specific manager belongs to.
        :param function_name: the name of the function that this specific manager belongs to, will be null in SSM case
        :param specific_manager_name: the actual name of specific manager (e.g., scaling, placement)
        :param id_number: the specific manager id number which is used to distinguish between multiple SSM/FSM
        that are created for the same objective (e.g., scaling with algorithm 1 and 2)
        :param updated_version: specifies whether this SM is developed to update a current version or not,should be
        filled either by 'true' or 'false'
        :param version: version
        :param description: description
        """
        #checks if the chosen name by develeopr is correct format
        self.name_validation(specific_manager_type, service_name, function_name, specific_manager_name, id_number)

        #Populating SSM-FSM fileds
        self.specific_manager_type = specific_manager_type
        self.service_name = service_name
        self.function_name = function_name
        self.specific_manager_name = specific_manager_name
        self.id_number = id_number
        if self.specific_manager_type == 'fsm':
            self.specific_manager_id = "son{0}{1}{2}{3}{4}".\
                format(specific_manager_type, service_name, function_name, specific_manager_name, id_number)
        else:
            self.specific_manager_id = "son{0}{1}{2}{3}".\
                format(specific_manager_type, service_name, specific_manager_name, id_number)
        self.version = version
        self.description = description
        self.update_version = update_version
        self.uuid = None
        self.sfuuid = None

        LOG.info("Starting {0} ...".format(self.specific_manager_id))

        # create and initialize broker connection
        self.manoconn = messaging.ManoBrokerRequestResponseConnection(self.specific_manager_id)

        self.tLock = threading.Lock()
        t1 = threading.Thread(target=self.registration)
        t2 = threading.Thread(target=self.run)

        # register to Specific Manager Registry
        t1.start()

        # locks the registration thread
        self.tLock.acquire()

        # jump to run
        t2.start()

    def name_validation(self, smtype, sname, fname, name, id):

        if smtype != 'ssm' and smtype != 'fsm':
            LOG.error("Invalid type: ({0}), specific_manager_type must be either ssm or fsm".format(smtype))
            exit(1)
        if not re.match("^[a-zA-Z0-9][a-zA-Z0-9_.-]*$", sname):
            LOG.error("Invalid service name: ({0}), only [a-zA-Z0-9][a-zA-Z0-9_.-] are allowed".format(sname))
            exit(1)
        if fname != None:
            if not re.match("^[a-zA-Z0-9][a-zA-Z0-9_.-]*$", fname):
                LOG.error("Invalid function name: ({0}), only [a-zA-Z0-9][a-zA-Z0-9_.-] are allowed".format(sname))
                exit(1)
        if not re.match("^[a-zA-Z0-9][a-zA-Z0-9_.-]*$", name):
            LOG.error("Invalid service name: ({0}), only [a-zA-Z0-9][a-zA-Z0-9_.-] are allowed".format(sname))
            exit(1)
        if not id.isdigit():
            LOG.error("Invalid id number: ({0}), only (0-9) are allowed".format(id))
            exit(1)


    def run(self):

        # go into infinity loop (we could do anything here)
        while True:
            time.sleep(1)

    def registration(self):

        """
        Send a register request to the Specific Manager registry.

        """
        self.tLock.acquire()
        message = {'specific_manager_type': self.specific_manager_type,
                   'service_name': self.service_name,
                   'function_name': self.function_name,
                   'specific_manager_name': self.specific_manager_name,
                   'specific_manager_id': self.specific_manager_id,
                   'update_version': self.update_version,
                   'version': self.version,
                   'description': self.description}
        self.manoconn.call_async(self._on_registration_response,
                                 'specific.manager.registry.ssm.registration',
                                 yaml.dump(message))

    def _on_registration_response(self, ch, method, props, response):

        response = yaml.load(str(response))
        if response['status'] != "registered":
            LOG.error("{0} registration failed. Exit".format(self.specific_manager_id))
        else:
            self.uuid = response['uuid']
            if 'sf_uuid' in os.environ:
                self.sfuuid = os.environ['sf_uuid']
            LOG.info("{0} registered with uuid:{1}".format(self.specific_manager_id, self.uuid))

            # release the registration thread
            self.tLock.release()

            # jump to on_registration_ok()
            self.on_registration_ok()


    def on_registration_ok(self):
        """
        To be overwritten by subclasses
        """
        LOG.debug("Received registration ok event.")
