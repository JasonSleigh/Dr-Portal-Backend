#!/bin/bash
# Load the docker-compose file
docker-compose -f /docker-compose.dev.yml up -d
# add a echo here for me to see when this is done
echo "Docker Compose is up and running"	


