#!/bin/bash


if [ "$1" == 'build' ]; then
    # build docker images
    docker build -t smart-plants .
elif [ "$1" == 'start' ]; then
  # export api_key
  source sendgrid.env
  docker run --name sp-webapp --network host -d -it --entrypoint bash smart-plants -c "python3 -u app.py"
  WEBAPP=$(docker ps -aqf "name=sp-webapp")
  echo -e "\nSmart Plants webapp is running. You can check the logs with 'docker logs -f ${WEBAPP}'"
  docker run --name sp-reporter -e SENDGRID_API_KEY="${SENDGRID_API_KEY}" --network host -d -it --entrypoint bash smart-plants  -c "python3 -u main.py"
  REPORTER=$(docker ps -aqf "name=sp-reporter")
  echo -e "\nSmart Plants reporter is running. You can check the logs with 'docker logs -f ${REPORTER}'"
elif [ "$1" == 'stop' ]; then
    # shellcheck disable=SC2046
    docker rm $(docker stop $(docker ps -a -q --filter ancestor=smart-plants --format="{{.ID}}"))
else
  echo "Options to pass are: build, start or stop"
  exit 1
fi



