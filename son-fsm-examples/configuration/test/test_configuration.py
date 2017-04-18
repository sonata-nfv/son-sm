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

import unittest
import yaml
import threading
import logging
import time
import sys

from multiprocessing import Process
import vnfrsender
import fake_smr
from sonmanobase import messaging
from configuration import configuration

logging.basicConfig(level=logging.INFO)
logging.getLogger('amqp-storm').setLevel(logging.INFO)
LOG = logging.getLogger("son-mano-plugins:sm_template_test")
logging.getLogger("son-mano-base:messaging").setLevel(logging.INFO)
LOG.setLevel(logging.INFO)




class testSMTemplate(unittest.TestCase):

    def setUp(self):

        self.manoconn = messaging.ManoBrokerRequestResponseConnection('ConfTest')

    def tearDown(self):
        pass

    def test_configuration_registration(self):


        def on_register_receive(ch, method, properties, message):

            if properties.app_id != 'fake-smr':
                msg = yaml.load(message)
                # CHECK: The message should be a dictionary.
                self.assertTrue(isinstance(msg, dict), msg='message is not a dictionary')
                # CHECK: The dictionary should have a key 'specific_manager_name'.
                self.assertIn('specific_manager_name', msg.keys(), msg='no specific_manager_name provided in message.')
                if isinstance(msg['specific_manager_name'], str):
                    # CHECK: The value of 'specific_manager_name' should not be an empty string.
                    self.assertTrue(len(msg['specific_manager_name']) > 0, msg='empty specific_manager_name provided.')
                else:
                    # CHECK: The value of 'specific_manager_name' should be a string
                    self.assertEqual(True, False, msg='specific_manager_name is not a string')
                # CHECK: The dictionary should have a key 'version'.
                self.assertIn('version', msg.keys(), msg='No version provided in message.')
                if isinstance(msg['version'], str):
                    # CHECK: The value of 'version' should not be an empty string.
                    self.assertTrue(len(msg['version']) > 0, msg='empty version provided.')
                else:
                    # CHECK: The value of 'version' should be a string
                    self.assertEqual(True, False, msg='version is not a string')
                # CHECK: The dictionary should have a key 'description'
                self.assertIn('description', msg.keys(), msg='No description provided in message.')
                if isinstance(msg['description'], str):
                    # CHECK: The value of 'description' should not be an empty string.
                    self.assertTrue(len(msg['description']) > 0, msg='empty description provided.')
                else:
                    # CHECK: The value of 'description' should be a string
                    self.assertEqual(True, False, msg='description is not a string')

                # CHECK: The dictionary should have a key 'specific_manager_type'
                if isinstance(msg['specific_manager_type'], str):
                    # CHECK: The value of 'specific_manager_type' should not be an empty string.
                    self.assertTrue(len(msg['specific_manager_type']) > 0, msg='empty specific_manager_type provided.')
                else:
                    # CHECK: The value of 'specific_manager_type' should be a string
                    self.assertEqual(True, False, msg='specific_manager_type is not a string')

                # CHECK: The dictionary should have a key 'service_name'
                if isinstance(msg['service_name'], str):
                    # CHECK: The value of 'service_name' should not be an empty string.
                    self.assertTrue(len(msg['service_name']) > 0, msg='empty service_name id provided.')
                else:
                    # CHECK: The value of 'service_name' should be a string
                    self.assertEqual(True, False, msg='service_name is not a string')

        def on_ip_receive(ch, method, properties, message):

            if properties.app_id == 'fake-smr':
                payload = yaml.load(message)

                self.assertTrue(isinstance(payload, dict), msg='message is not a dictionary')

                if isinstance(payload['IP'], str):
                    self.assertTrue(payload['IP'] == "10.100.32.250", msg='Wrong IP address')
                else:
                    self.assertEqual(True, False, msg='IP address is not a string')

        fake_smr.main()

        self.manoconn.subscribe(on_register_receive, 'specific.manager.registry.ssm.registration')

        time.sleep(4)

        configuration.main()

        self.manoconn.subscribe(on_ip_receive, 'son.configuration')
        time.sleep(4)

        vnfrsender.main()




if __name__ == '__main__':
    unittest.main()