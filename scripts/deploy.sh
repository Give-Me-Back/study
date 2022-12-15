#!/bin/bash
echo 12/15 TEST
cd /home/ubuntu/GMB/COKO
sudo gunicorn --bind 0.0.0.0:8000 config.wsgi:application --daemon