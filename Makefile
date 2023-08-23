all: build 

COMPOSE_FILE=./docker/docker-compose.yml

####################################################################################################
# Docker Compose vars 
#---------------------------------------------------------------------------------------------------

CONTEXT=app

MAIN_SERVICE=${CONTEXT}.front
BACKEND_SERVICE=${CONTEXT}.back

####################################################################################################
# Docker Compose Commands 
#---------------------------------------------------------------------------------------------------

DOCKER_COMPOSE=docker-compose -f ${COMPOSE_FILE}

DOCKER_COMPOSE_RUN=${DOCKER_COMPOSE} run --rm --service-ports
DOCKER_COMPOSE_UP=${DOCKER_COMPOSE} up --remove-orphans
DOCKER_COMPOSE_BUILD=${DOCKER_COMPOSE} build

#--------------------------------------------------------------------------------------------------
#--- ( Main Commands ) ----------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

build:
	echo ${DOCKER_DEFAULT_PLATFORM}
	${DOCKER_COMPOSE_BUILD} ${MAIN_SERVICE}

run:
	${DOCKER_COMPOSE_UP} ${MAIN_SERVICE}

run_front:
	${DOCKER_COMPOSE_UP} ${MAIN_SERVICE}

run_back:
	${DOCKER_COMPOSE_UP} ${BACKEND_SERVICE}

stop_containers:
	docker rm -f $(shell docker ps -aq)

#--------------------------------------------------------------------------------------------------
#--- ( Helper Commands ) -------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

bash:
	${DOCKER_COMPOSE_RUN} --entrypoint bash ${MAIN_SERVICE}

python:
	${DOCKER_COMPOSE_RUN} --entrypoint python ${MAIN_SERVICE}

init:
	${DOCKER_COMPOSE_RUN} --entrypoint "reflex init" ${MAIN_SERVICE}
