# Function Specific Manager (FSM) Example
A FSM example (configuration fsm) that connects to Service Specific Manager(SMR) and register itself using the SSM/FSM template.

## Requires
* Docker

## Implementation
* implemented in Python 3.4
* dependecies: amqp-storm
* The main implementation can be found in: `son-fsm-examples/configuration/configuration.py`

## How to run it

* To run the configuration FSM locally, you need:
 * a running RabbitMQ broker (see general README.md of [son-mano framework repository](https://github.com/sonata-nfv/son-mano-framework) for info on how to do this)
 * a running Service Specific Registry (SMR) connected to the broker (see general README.md of [SMR repository](https://github.com/sonata-nfv/son-mano-framework) for info on how to do this)

* Run the configuration FSM (directly in your terminal not in a Docker container):
 * (do in `son-sm/`)
 * `python3.4 son-fsm-examples-configuration/configuration/configuration.py`

* Or: run the configuration FSM (in a Docker container):
 * (do in `son-sm/`)
 * `docker build -t sonfsmfunctionconfiguration1 -f son-fsm-examples/configuration/Dockerfile .`
 * `docker run -it --rm --link broker:broker  --name sonfsmfunctionconfiguration1  sonfsmfunctionconfiguration1`
