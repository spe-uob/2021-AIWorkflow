#!/bin/bash
# build_container.sh <port>
FILE=Dockerfile
if [ ! -f "$FILE" ]
then
    echo "$FILE does not exist"
    echo "Exit script"
    exit 1
fi
BUILD_DATE=`date -u +'%Y-%m-%dT%H:%M:%SZ'`
COMMIT_ID=$(git rev-parse --verify HEAD)
COMMIT_ID=${COMMIT_ID:0:8}
VER=`date -u +'%Y%m%d'`
VER="${VER}_${COMMIT_ID}"
TAG=${PWD##*/}
DIR=$2
sudo docker build --build-arg BUILD_DATE=$BUILD_DATE --build-arg TITLE=$TAG -t $TAG:$VER .
EXIST=`sudo docker inspect --format "{{ index .Config.Labels \"org.opencontainers.image.title\"}}" $TAG`
if [ "$TAG" == "$EXIST" ]
then
    echo "Container with the same name is found."
    HOME=`getent passwd $USER | awk -F ':' '{print $6}'`
    LOG_DIR=${HOME}/logs
    echo $log_dir
    if [ ! -d  "$LOG_DIR" ]
    then
        echo "Directory does not exist. Make directory."
        mkdir $LOG_DIR
    fi
    echo "Backing up log to ~/logs"
    LOG_PATH=`docker inspect --format='{{.LogPath}}' $TAG`
    LOG_FILENAME=`basename $LOG_PATH`
    sudo cp $LOG_PATH $LOG_DIR
    OLD_IMG_TAG=`sudo docker image ls --format '{{.Tag}}' $TAG | head -1`
    OLD_CONTAINER_ID=`echo $(sudo docker inspect --format "{{.Id}}" $TAG) | cut -c1-12`
    NEW_LOG_FILENAME="${TAG}_${OLD_IMG_TAG}_${OLD_CONTAINER_ID}.log"
    mv "${LOG_DIR}/${LOG_FILENAME}" "${LOG_DIR}/${NEW_LOG_FILENAME}"
    sudo chmod a+rwx "${LOG_DIR}/${NEW_LOG_FILENAME}"

    echo "Removing container."
    sudo docker stop $TAG > /dev/null
    sudo docker rm $TAG
fi
if [ $# -eq 0 ]
then
    DOCKER_HOST_PORT=5008
    echo "argument Docker Host Port not provided. Port set to $DOCKER_HOST_PORT by default"
else
    DOCKER_HOST_PORT=$1
fi
APP_PORT=80

# environment variables
TIMEZONE="TZ=Asia/Hong_Kong"
MODULE_NAME="MODULE_NAME=application" # for uvicorn, if main file was at /app/custom_app/custom_main.py >>> MODULE_NAME="custom_app.custom_main"
MAX_WORKERS="MAX_WORKERS=1"
TIMEOUT="TIMEOUT=3600"

sudo docker run -d --name $TAG -p $DOCKER_HOST_PORT:$APP_PORT --restart unless-stopped -e $MAX_WORKERS -e $TIMEOUT -e $TIMEZONE -e $MODULE_NAME $TAG:$VER
