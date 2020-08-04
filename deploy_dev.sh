#!/bin/bash

docker stop redis
docker run --rm -d -p 6379:6379 --name redis redis
cd app
./manage.py runserver
# daphne -b 0.0.0.0 -p 8000 config.asgi:application
