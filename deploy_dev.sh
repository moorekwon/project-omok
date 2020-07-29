#!/bin/bash

docker stop redis
docker system prune -f
docker run --rm -d -p 6379:6379 --name redis redis
cd app
./manage.py runserver
