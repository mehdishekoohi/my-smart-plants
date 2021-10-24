#!/bin/bash

CPU=$(uname -m)

if [[ $CPU == *"x86_64"* ]]; then
  ARCH="amd"
elif [[ $CPU == *"arm"* ]]; then
  ARCH="arm"
  SOURCE="arm32v7/"
else
  # "Unknown CPU architecture"
  ARCH="amd"
fi


if [ "$1" == 'build' ]; then
    echo -e "Building image for '${ARCH}' architecture"
    # build docker images
    docker build --build-arg SOURCE=$SOURCE -t smart-plants .
elif [ "$1" == 'start-webapp' ]; then
  docker run -v /dev/ttyACM0:/dev/ttyACM0 \
        --privileged \
        --restart=always \
        --name sp-webapp \
        --network host -d -it \
        --entrypoint bash \
        smart-plants -c "python3 -u app.py"

  WEBAPP=$(docker ps -aqf "name=sp-webapp")
  MACHINE_IP=$(hostname -I | cut -d' ' -f1)
  echo -e "\nCTRL+Click http://${MACHINE_IP}:5000 to see plants stats."
  echo -e "\nSmart Plants webapp is running. You can check the logs with 'docker logs -f ${WEBAPP}'\n"

elif [ "$1" == 'start-reporter' ]; then
  # export api_key
  source sendgrid.env
  docker run -v /dev/ttyACM0:/dev/ttyACM0 \
        --privileged \
        --name sp-reporter \
        --restart=always \
        -e SENDGRID_API_KEY="${SENDGRID_API_KEY}" \
        --network host -d -it \
        --entrypoint bash \
        smart-plants  -c "python3 -u main.py"

  REPORTER=$(docker ps -aqf "name=sp-reporter")
  echo -e "\nSmart Plants reporter is running. You can check the logs with 'docker logs -f ${REPORTER}'\n"
elif [ "$1" == 'stop' ]; then
    # shellcheck disable=SC2046
    docker rm $(docker stop $(docker ps -a -q --filter ancestor=smart-plants --format="{{.ID}}"))
else
  echo "Options to pass are: build, start-webapp, start-reporter or stop"
  exit 1
fi