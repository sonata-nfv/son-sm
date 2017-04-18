# Updating an SSM Example (in progress)
An example that updates the dumb SSM (in progress)

## Requires
* Docker
* Python3.4
* RabbitMQ

## Implementation
* Implemented in Python 3.4
* Dependencies: amqp-storm

## Build
`docker build -t sonfsmservice1updateddumb1 -f son-ssm-examples/updating/Dockerfile .`

## Run
`docker run -it --rm --link broker:broker --name sonfsmservice1updateddumb1 sonfsmservice1updateddumb1`