#!/usr/bin/env bash

# Copyright (c) 2015 SONATA-NFV
# ALL RIGHTS RESERVED.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Neither the name of the SONATA-NFV [, ANY ADDITIONAL AFFILIATION]
# nor the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written
# permission.
#
# This work has been performed in the framework of the SONATA project,
# funded by the European Commission under Grant number 671517 through
# the Horizon 2020 and 5G-PPP programmes. The authors would like to
# acknowledge the contributions of their colleagues of the SONATA
# partner consortium (www.sonata-nfv.eu).

# This script runs the SSM/FSM template related tests.
#
# It starts three Docker containers:
# - RabbitMQ
# It triggers the unittest execution in son-sm-template
#

# setup cleanup mechanism
trap "set +e; docker rm -fv test.broker; docker rm -fv test.sonfsmservice1firewallconfiguration1 " INT TERM EXIT

# ensure cleanup
set +e
docker rm -fv test.broker
docker rm -fv test.sonfsmservice1firewallconfiguration1
#  always abort if an error occurs
set -e

echo "test_son-sm-template.sh"
# spin up container with broker (in daemon mode)
docker run -d -p 5672:5672 --name test.broker rabbitmq:3
# wait a bit for broker startup
while ! nc -z localhost 5672; do
sleep 1 && echo -n .; # waiting for rabbitmq
done;

sleep 3

docker run --link test.broker:broker --name test.sonfsmservice1firewallconfiguration1 sonfsmservice1firewallconfiguration1 py.test -v


echo "done."