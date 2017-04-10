# Monitoring FSM Example
A monitoring FSM example that connects to Service Specific Manager (SMR) and performs a self-registration using the SSM / FSM template. Once the registration is done, it subscribes to the son.monitoring topic to receive monitoring alerts. It then filters the alerts and only reacts to CPU usage alerts.

## Requires
* Docker
* Python3.4
* RabbitMQ

## Implementation
* Implemented in Python 3.4
* Dependencies: amqp-storm
* The main implementation can be found in: `son-fsm-examples/monitoring/monitoring.py`

## How to run it

* To run the monitoring FSM locally, you need:
 * a running RabbitMQ broker (see general README.md of [son-mano framework repository](https://github.com/sonata-nfv/son-mano-framework) for info on how to do this)
 * a running Service Specific Registry (SMR) connected to the broker (see general README.md of [SMR repository](https://github.com/sonata-nfv/son-mano-framework) for info on how to do this)

* Run the monitoring FSM (in a Docker container):
 * (do in `son-sm/`)
 * `docker build -t sonfsmservice1function1monitoring1 -f son-fsm-examples/monitoring/Dockerfile .`
 * `docker run -it --rm --link broker:broker  --name sonfsmservice1function1monitoring1  sonfsmservice1function1monitoring1`

* Or: Run the monitoring FSM (directly in your terminal not in a Docker container):
 * (In `son-sm/son-sm-template/`)
    * `python3.4 setup.py install`
 * (In `son-sm/son-fsm-examples/monitoring/`)
    * `python3.4 setup.py develop`
 * (In `son-sm/`)
    * `python3.4 son-fsm-examples/monitoring/monitoring/monitoring.py`

## How to test it
* Do the following; each in a separate terminal.
    1. Run the SMR container
    2. Run the monitoring container
    3. In son-sm/son-fsm-examples/monitoring/test run python3.4 alertsender.py

* The expected results are as follows:

    * In the SMR terminal:

        ```
        DEBUG:son-mano-specific-manager-registry:registration request received for: sonfsmservice1function1monitoring1
        INFO:son-mano-specific-manager-registry:sonfsmservice1function1monitoring1 status: Subscribed to son.monitoring topic, waiting for alert message
        INFO:son-mano-specific-manager-registry:sonfsmservice1function1monitoring1 status: cpu usage 85% alert message received
        ```

    * In monitoring terminal:

         ```
         INFO:son-sm-base:Starting sonfsmservice1function1monitoring1 ...
         INFO:son-sm-base:sonfsmservice1function1monitoring1 registered with uuid:585ab9d7-70f1-43f5-8370-2f320fc08361
         DEBUG:fsm-monitoring-1:Received registration ok event.
         DEBUG:fsm-monitoring-1:Subscribed to son.monitoring topic.
         WARNING:amqpstorm.channel:Received Basic.Cancel on consumer_tag: q.specific.manager.registry.ssm.registration.68c8fe97-9c63-4b7a-a398-273d37b2e2d6
         INFO:fsm-monitoring-1:Alert message received
         ```
