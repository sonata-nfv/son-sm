# Updating an FSM example (in progress)
An example that updates the dumb FSM

## Requires
* Docker
* Python3.4
* RabbitMQ

## Implementation
* Implemented in Python 3.4
* Dependencies: amqp-storm
* The main implementation can be found in: `son-fsm-examples/dumb/dumb.py`

## How to run it

* To run the dumb FSM locally, you need:
 * a running RabbitMQ broker (see general README.md of [son-mano framework repository](https://github.com/sonata-nfv/son-mano-framework) for info on how to do this)
 * a running Service Specific Registry (SMR) connected to the broker (see general README.md of [SMR repository](https://github.com/sonata-nfv/son-mano-framework) for info on how to do this)

* Run the dumb FSM (in a Docker container):
 * (do in `son-sm/`)
 * `docker build -t sonfsmservice1function1updateddumb1 -f son-fsm-examples/updating/Dockerfile .`
 * `docker run -it --rm --link broker:broker  --name sonfsmservice1function1dumb1  sonfsmservice1function1updateddumb1`

* Or: Run the dumb FSM (directly in your terminal not in a Docker container):
 * (In `son-sm/son-sm-template/`)
    * `python3.4 setup.py install`
 * (In `son-sm/son-fsm-examples/dumb/`)
    * `python3.4 setup.py develop`
 * (In `son-sm/`)
    * `python3.4 son-fsm-examples/dumb/dumb/dumb.py`

## How to test it
* Do the following; each in a separate terminal.
    1. Run the SMR container
    2. Run the dumb container

* The expected results are as follows:

    * In the SMR terminal:

        ```
        DEBUG:son-mano-specific-manager-registry:registration request received for: sonfsmservice1function1dumb1
        INFO:son-mano-specific-manager-registry:sonfsmservice1function1dumb1 status: UP and Running
        ```

    * In dumb terminal:

         ```
         INFO:son-sm-base:Starting sonfsmservice1function1dumb1 ...
         INFO:son-sm-base:sonfsmservice1function1dumb1 registered with uuid:1a4315bb-398d-441c-9ae2-bae517974c75
         DEBUG:fsm-dumb-1:Received registration ok event.
         WARNING:amqpstorm.channel:Received Basic.Cancel on consumer_tag: q.specific.manager.registry.ssm.registration.885523eb-553d-4832-bbae-fbbd90cbf325
         ```
