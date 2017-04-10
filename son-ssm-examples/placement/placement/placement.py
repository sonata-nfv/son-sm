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
from sonsmbase.smbase import sonSMbase

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("ssm-placement-1")
LOG.setLevel(logging.DEBUG)
logging.getLogger("son-mano-base:messaging").setLevel(logging.INFO)


class PlacementSSM(sonSMbase):

    def __init__(self):

        """
        :param specific_manager_type: specifies the type of specific manager that could be either fsm or ssm.
        :param service_name: the name of the service that this specific manager belongs to.
        :param function_name: the name of the function that this specific manager belongs to, will be null in SSM case
        :param specific_manager_name: the actual name of specific manager (e.g., scaling, placement)
        :param id_number: the specific manager id number which is used to distinguish between multiple SSM/FSM
        that are created for the same objective (e.g., scaling with algorithm 1 and 2)
        :param version: version
        :param description: description
        """
        self.specific_manager_type = 'ssm'
        self.service_name = 'service1'
        self.specific_manager_name = 'placement'
        self.id_number = '1'
        self.version = 'v0.1'
        self.description = "Placement SSM"

        super(self.__class__, self).__init__(specific_manager_type= self.specific_manager_type,
                                             service_name= self.service_name,
                                             specific_manager_name = self.specific_manager_name,
                                             id_number = self.id_number,
                                             version = self.version,
                                             description = self.description)


    def on_registration_ok(self):

        LOG.debug("Received registration ok event.")

        # For testing, here we set the service uuid.
        # In the actual scenario this should be set by SLM and SMR during the SSM instantiation.
        self.sfuuid = '1234'

        # Register to placement topic.
        topic = 'placement.ssm.' + self.sfuuid

        self.manoconn.register_async_endpoint(self.on_place,topic= topic)

        LOG.info("Subscribed to {0}".format(topic))

    def on_place(self, ch, method, properties, payload):


        if properties.app_id != self.specific_manager_id:

            LOG.info("Placement request received: {0}".format(payload))
            payload = {'placement': ['from_ssm']}
            LOG.info("Placement decision was sent: {0}".format(payload))

            # send the status to the SMR (not necessary)
            self.manoconn.publish(topic='specific.manager.registry.ssm.status', message=yaml.dump(
                {'name': self.specific_manager_id, 'status': "Placement decision was sent: {0}".format(payload)}))

        return (yaml.dump(payload))

def main():
    PlacementSSM()

if __name__ == '__main__':
    main()
