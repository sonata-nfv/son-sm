# Function Specific Manager (FSM) Example
A monitoring FSM example that connects to Service Specific Manager (SMR) and registers itself using the SSM / FSM template. Once the registration is done, it subscribes to the son.monitoring topic to receive monitoring alerts.

## Requires
* Docker

## Implementation
* implemented in Python 3.4
* dependecies: amqp-storm
* The main implementation can be found in: `son-fsm-examples/monitoring/monitoring.py`

## How to run it

* To run the monitoring FSM locally, you need:
 * a running RabbitMQ broker (see general README.md of [son-mano framework repository](https://github.com/sonata-nfv/son-mano-framework) for info on how to do this)
 * a running Service Specific Registry (SMR) connected to the broker (see general README.md of [SMR repository](https://github.com/sonata-nfv/son-mano-framework) for info on how to do this)

* Run the monitoring FSM (directly in your terminal not in a Docker container):
 * (do in `son-sm/`)
 * `python3.4 son-fsm-examples-monitoring/monitoring/monitoring.py`

* Or: run the monitoring FSM (in a Docker container):
 * (do in `son-sm/`)
 * `docker build -t sonfsmfunctionmonitoring1 -f son-fsm-examples/monitoring/Dockerfile .`
 * `docker run -it --rm --link broker:broker  --name sonfsmfunctionmonitoring1  sonfsmfunctionmonitoring1`
