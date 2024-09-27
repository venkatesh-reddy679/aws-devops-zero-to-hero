#! /bin/bash
echo "getting the containerID and stopping it"
docker ps
containerID=$(docker ps | grep pythonapp | awk '{ print $1 }')

if [[ -n $containerID ]]; then
  docker rm -f $containerID
  docker system prune -a
fi
docker ps
