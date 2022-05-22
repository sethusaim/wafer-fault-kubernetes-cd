#!bin/bash

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 347460842118.dkr.ecr.us-east-1.amazonaws.com

if [ "$DOCKERTAG" == "1" ];then
    docker run -p 8080:8080 --name wafer_app 347460842118.dkr.ecr.us-east-1.amazonaws.com/$REPO_NAME:$DOCKERTAG
else
    docker stop wafer_app && docker rm wafer_app && docker run -p 8080:8080 --name wafer_app 347460842118.dkr.ecr.us-east-1.amazonaws.com/$REPO_NAME:$DOCKERTAG
fi