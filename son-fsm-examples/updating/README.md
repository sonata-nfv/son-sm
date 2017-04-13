# Updating an FSM example (in progress)
An example that updates the dumb FSM

## Requires
* Docker
* Python3.4
* RabbitMQ

## Implementation
* Implemented in Python 3.4
* Dependencies: amqp-storm

## Build
`docker build -t sonfsmservice1function1updateddumb1 -f son-fsm-examples/updating/Dockerfile .`


## Run
`docker run -it --rm --link broker:broker --name sonfsmservice1function1updateddumb1 sonfsmservice1function1updateddumb1`
