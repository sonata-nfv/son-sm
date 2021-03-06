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
import json
import time
from sonmanobase import messaging

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("son-mano-fakeslm")
LOG.setLevel(logging.DEBUG)
logging.getLogger("son-mano-base:messaging").setLevel(logging.INFO)


class fakealert(object):
    def __init__(self):

        self.name = 'fake-alert'
        self.version = '0.1-dev'
        self.description = 'description'

        LOG.info("Starting alert:...")

        # create and initialize broker connection
        self.manoconn = messaging.ManoBrokerRequestResponseConnection(self.name)

        self.path_descriptors = 'test/test_descriptors/'
        self.end = False

        self.publish_nsd()

        self.run()

    def run(self):

        # go into infinity loop

        while self.end == False:
            time.sleep(1)

    def publish_nsd(self):

        LOG.info("Sending alert request")

        message = {"exported_instance": "fw-vnf","core": "cpu","group": "development","exported_job": "vnf","value": "1",
                   "instance": "pushgateway:9091","job": "sonata","serviceID": "263fd6b7-8cfb-4149-b6c1-fb082553ca71",
                   "alertname": "mon_rule_vm_cpu_usage_85_perc","time": "2016-09-13T17:29:22.807Z","inf": "None","alertstate": "firing",
                   "id": "01ccc69f-c925-42f5-9418-e1adb075527e","monitor": "sonata-monitor"}


        self.manoconn.publish('son.monitoring',json.dumps(message))


def main():
    fakealert()


if __name__ == '__main__':
    main()