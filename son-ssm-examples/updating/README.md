# Updating an SSM Example (in progress)
An example that updates the dumb SSM (in progress)
## Requires
* Docker
* Python3.4
* RabbitMQ

## Implementation
* Implemented in Python 3.4
* Dependencies: amqp-storm
* The main implementation can be found in: `son-ssm-examples/dumb/dumb.py`

## How to run it

* To run the dumb SSM locally, you need:
 * a running RabbitMQ broker (see general README.md of [son-mano framework repository](https://github.com/sonata-nfv/son-mano-framework) for info on how to do this)
 * a running Service Specific Registry (SMR) connected to the broker (see general README.md of [SMR repository](https://github.com/sonata-nfv/son-mano-framework) for info on how to do this)

* Run the dumb SSM (in a Docker container):
 * (do in `son-sm/`)
 * `docker build -t sonssmservice1updateddumb1 -f son-ssm-examples/updating/Dockerfile .`
 * `docker run -it --rm --link broker:broker  --name sonssmservice1dumb1  sonssmservice1dumb1`

* Or: Run the dumb SSM (directly in your terminal not in a Docker container):
 * (In `son-sm/son-sm-template/`)
    * `python3.4 setup.py install`
 * (In `son-sm/son-ssm-examples/dumb/`)
    * `python3.4 setup.py develop`
 * (In `son-sm/`)
    * `python3.4 son-ssm-examples/dumb/dumb/dumb.py`

## How to test it
* Do the following; each in a separate terminal.
    1. Run the SMR container
    2. Run the dumb container

* The expected results are as follows:

    * In the SMR terminal:

        ```
        DEBUG:son-mano-specific-manager-registry:registration request received for: sonssmservice1dumb1
        INFO:son-mano-specific-manager-registry:sonssmservice1dumb1 status: UP and Running
        ```

    * In dumb terminal:

         ```
         INFO:son-sm-base:Starting sonssmservice1dumb1 ...
         INFO:son-sm-base:sonssmservice1dumb1 registered with uuid:9c370603-c0de-43bc-8d40-01b886e3190a
         DEBUG:ssm-dumb-1:Received registration ok event.
         WARNING:amqpstorm.channel:Received Basic.Cancel on consumer_tag: q.specific.manager.registry.ssm.registration.b3fd95d4-2550-4d5d-ba34-9bc58a0f07f3
         ```
