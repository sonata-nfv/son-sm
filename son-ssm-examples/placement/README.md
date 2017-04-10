# Placement SSM Example (in progress)
An example of placement SSM taking care of service placement.

## Requires
* Docker
* Python3.4
* RabbitMQ

## Implementation
* Implemented in Python 3.4
* Dependencies: amqp-storm
* The main implementation can be found in: `son-ssm-examples/placement/placement.py`

## How to run it

* To run the placement SSM locally, you need:
 * a running RabbitMQ broker (see general README.md of [son-mano framework repository](https://github.com/sonata-nfv/son-mano-framework) for info on how to do this)
 * a running Service Specific Registry (SMR) connected to the broker (see general README.md of [SMR repository](https://github.com/sonata-nfv/son-mano-framework) for info on how to do this)

* Run the placement SSM (in a Docker container):
 * (do in `son-sm/`)
 * `docker build -t sonssmservice1placement1 -f son-ssm-examples/placement/Dockerfile .`
 * `docker run -it --rm --link broker:broker  --name sonssmservice1placement1  sonssmservice1placement1`

* Or: Run the placement SSM (directly in your terminal not in a Docker container):
 * (In `son-sm/son-sm-template/`)
    * `python3.4 setup.py install`
 * (In `son-sm/son-ssm-examples/placement/`)
    * `python3.4 setup.py develop`
 * (In `son-sm/`)
    * `python3.4 son-ssm-examples/placement/placement/placement.py`

## How to test it
* Do the following; each in a separate terminal.
    1. Run the SMR container
    2. Run the placement container
    3. In son-sm/son-ssm-examples/placement/test run python3.4 placementtrigger.py

* The expected results are as follows:

    * In the SMR terminal:

        ```
        DEBUG:son-mano-specific-manager-registry:registration request received for: sonssmservice1placement1
        INFO:son-mano-specific-manager-registry:sonssmservice1placement1 status: Placement decision was sent: {'placement': ['from_ssm']}
        ```

    * In placement terminal:

         ```
         INFO:son-sm-base:Starting sonssmservice1placement1 ...
         INFO:son-sm-base:sonssmservice1placement1 registered with uuid:d88f37a2-6ca4-47cb-a103-833f5fc29fb9
         DEBUG:ssm-placement-1:Received registration ok event.
         INFO:ssm-placement-1:Subscribed to placement.ssm.1234
         WARNING:amqpstorm.channel:Received Basic.Cancel on consumer_tag: q.specific.manager.registry.ssm.registration.2e50cc94-abc8-4663-b1dc-91c12c6a10fa
         INFO:ssm-placement-1:Placement request received: {cpu: '20', location: DE, memory: '30'}
         INFO:ssm-placement-1:Placement decision was sent: {'placement': ['from_ssm']}
         ```
