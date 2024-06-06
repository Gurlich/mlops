#!/bin/bash

# use this script to build with resolving .env-files with docker-copmose.yaml
# execute this script from directory with .env and docker-compose file 

set -a
. .env.dev

docker compose build
