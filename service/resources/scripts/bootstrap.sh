#!/bin/bash


if [ "$REFLEX_ENV" = "frontend" ]; then
    echo 'Starting app frontend only'
    params='--frontend-only && tail -f version.json'
elif [ "$REFLEX_ENV" = "backend" ]; then
    echo 'Starting app backend only'
    params='--backend-only'
fi

# Checks if the .web directory was created, if not, we run a PC init to create it
#
# Note: the Dockerfile is already running this command, but we need to run this to create the 
# directories and dependencies in local env too

ls -lha | grep .web && echo 'Reflex already initialized'|| reflex init 

bash -c "reflex run $params"
