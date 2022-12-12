#!/bin/bash
cd /home/ubuntu/GMB/COKO
sudo echo test!
sudo gunicorn --bind 0.0.0.0:8000 config.wsgi:application --daemon