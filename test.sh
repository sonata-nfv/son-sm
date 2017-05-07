#!/usr/bin/env bash

set +e
docker rm -fv sonfsmservice1firewallconfiguration1
docker rm -fv sonfsmservice1function1dumb1
docker rm -fv sonfsmservice1function1monitoring1
docker rm -fv sonfsmservice1function1updateddumb1
docker rm -fv sonssmservice1dumb1
docker rm -fv sonssmservice1placement1
docker rm -fv sonssmservice1dumb1

set +e
docker rmi -f hadik3r/sonfsmservice1firewallconfiguration1
docker rmi -f hadik3r/sonfsmservice1function1dumb1
docker rmi -f hadik3r/sonfsmservice1function1monitoring1
docker rmi -f hadik3r/sonfsmservice1function1updateddumb1
docker rmi -f hadik3r/sonssmservice1dumb1
docker rmi -f hadik3r/sonssmservice1placement1
docker rmi -f hadik3r/sonssmservice1updateddumb1


#set +e
#docker build -t hadik3r/sonfsmservice1firewallconfiguration1 -f son-fsm-examples/configuration/Dockerfile .
#docker build -t hadik3r/sonfsmservice1function1dumb1 -f son-fsm-examples/dumb/Dockerfile .
#docker build -t hadik3r/sonfsmservice1function1monitoring1 -f son-fsm-examples/monitoring/Dockerfile .
#docker build -t hadik3r/sonfsmservice1function1updateddumb1 -f son-fsm-examples/updating/Dockerfile .
#docker build -t hadik3r/sonssmservice1dumb1 -f son-ssm-examples/dumb/Dockerfile .
#docker build -t hadik3r/sonssmservice1placement1 -f son-ssm-examples/placement/Dockerfile .
#docker build -t hadik3r/sonssmservice1updateddumb1 -f son-ssm-examples/updating/Dockerfile .
#
#set -e
#
#docker push hadik3r/sonfsmservice1firewallconfiguration1
#docker push hadik3r/sonfsmservice1function1dumb1
#docker push hadik3r/sonfsmservice1function1monitoring1
#docker push hadik3r/sonfsmservice1function1updateddumb1
#docker push hadik3r/sonssmservice1dumb1
#docker push hadik3r/sonssmservice1placement1
#docker push hadik3r/sonssmservice1updateddumb1
#
#set +e
#docker rmi -f hadik3r/sonfsmservice1firewallconfiguration1
#docker rmi -f hadik3r/sonfsmservice1function1dumb1
#docker rmi -f hadik3r/sonfsmservice1function1monitoring1
#docker rmi -f hadik3r/sonfsmservice1function1updateddumb1
#docker rmi -f hadik3r/sonssmservice1dumb1
#docker rmi -f hadik3r/sonssmservice1placement1
#docker rmi -f hadik3r/sonssmservice1updateddumb1