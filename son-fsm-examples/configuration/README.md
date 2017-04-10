# Configuration FSM Example
A configuration FSM example that connects to Service Specific Manager(SMR) and performs a self-registration using the SSM/FSM template. Once the registration is done, it subscribes to configuration topic (son.configuration) to receive the VNFR which is sent by the SLM. Finally, it retrieves the VNF's IP address from the VNFR so that it can connect to the VNF and configure/reconfigure it.

## Requires
* Docker
* Python3.4
* RabbitMQ

## Implementation
* Implemented in Python 3.4
* Dependencies: amqp-storm
* The main implementation can be found in: `son-fsm-examples/configuration/configuration.py`

## How to run it

* To run the configuration FSM locally, you need:
 * a running RabbitMQ broker (see general README.md of [son-mano framework repository](https://github.com/sonata-nfv/son-mano-framework) for info on how to do this)
 * a running Service Specific Registry (SMR) connected to the broker (see general README.md of [SMR repository](https://github.com/sonata-nfv/son-mano-framework) for info on how to do this)

* Run the configuration FSM (in a Docker container):
 * (do in `son-sm/`)
 * `docker build -t sonfsmservice1firewallconfiguration1 -f son-fsm-examples/configuration/Dockerfile .`
 * `docker run -it --rm --link broker:broker  --name sonfsmservice1firewallconfiguration1  sonfsmservice1firewallconfiguration1`

* Or: Run the configuration FSM (directly in your terminal not in a Docker container):
 * (In `son-sm/son-sm-template/`)
    * `python3.4 setup.py install`
 * (In `son-sm/son-fsm-examples/configuration/`)
    * `python3.4 setup.py develop`
 * (In `son-sm/`)
    * `python3.4 son-fsm-examples/configuration/configuration/configuration.py`

## How to test it
* Do the following; each in a separate terminal.
    1. Run the SMR container
    2. Run the configuration container
    3. In son-sm/son-fsm-examples/configuration/test run python3.4 vnfrsender.py
* The expected results are as follows:

    * In the SMR terminal:

        ```
        DEBUG:son-mano-specific-manager-registry:registration request received for: sonfsmservice1firewallconfiguration1
        INFO:son-mano-specific-manager-registry:sonfsmservice1firewallconfiguration1 status: Registration is done, initialising the configuration...
        INFO:son-mano-specific-manager-registry:sonfsmservice1firewallconfiguration1 status: IP address:'10.100.32.250'
        ```

    * In configuration terminal:

         ```
         INFO:son-sm-base:Starting sonfsmservice1firewallconfiguration1 ...
         INFO:son-sm-base:sonfsmservice1firewallconfiguration1 registered with uuid:5e004db9-2bb2-460c-970a-0c8f08d21520
         DEBUG:fsm-configuration-1:Received registration ok event.
         WARNING:amqpstorm.channel:Received Basic.Cancel on consumer_tag: q.specific.manager.registry.ssm.registration.bf85aac3-a261-459d-afaa-c308e16fa289
         INFO:fsm-configuration-1:Start retrieving the IP address ...
         INFO:fsm-configuration-1:IP address:'10.100.32.250'
         ```
