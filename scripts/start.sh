#!/bin/bash

set -a
. .env.dev

# PROJECT_NAME=mlops \
# PROJECT_NAME=homework_03 \
PROJECT_NAME=homework_03 \
  MAGE_CODE_PATH=/home/src \
  SMTP_EMAIL=$SMTP_EMAIL \
  SMTP_PASSWORD=$SMTP_PASSWORD \
  docker compose up
