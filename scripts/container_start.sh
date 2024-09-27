#! /bin/bash

echo "this script is to run the container by pulling the docker image from AWS ECR"

docker pull 084828606525.dkr.ecr.us-east-2.amazonaws.com/test-image:8
docker run -dt -p 5000:5000 --name pythonapp 084828606525.dkr.ecr.us-east-2.amazonaws.com/test-image:8
docker ps

echo "container is created and port 5000 is exposed"
