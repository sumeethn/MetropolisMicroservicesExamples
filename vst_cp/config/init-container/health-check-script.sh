#!/bin/bash
apt-get update
apt-get install -y netcat
# set -e
export LC_ALL=C.UTF-8
export LANG=C.UTF-8


IFS=', ' read -r -a array <<< "$PORTS"

for port in "${array[@]}"
do  
   until nc -vz localhost $port; do echo "Waiting for service on port $port"; sleep 2; done;
   echo "port $port is reachable and service is up and running..."
done

echo "All ports reachable..."
exit 0
