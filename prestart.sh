#! /usr/bin/env bash

sleep 3;
python manage.py makemigrations

sleep 3;
python manage.py migrate

sleep 3;
# Run migrations
python manage.py runserver 0.0.0.0:8000