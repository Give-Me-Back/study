#!/bin/bash
cd /home/ubuntu/GMB/COKO
sudo gunicorn --bind 0.0.0.0:8000 config.wsgi:application --daemon
echo 12/14