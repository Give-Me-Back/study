#!/bin/bash
sudo rm -rf /home/ubuntu/GMB/COKO/templates
sudo rm -rf /home/ubuntu/GMB/COKO/config/urls.py
sudo rm -rf /home/ubuntu/GMB/COKO/static
sudo mv /home/ubuntu/app/scripts/templates /home/ubuntu/GMB/COKO/
sudo mv /home/ubuntu/app/scripts/urls.py /home/ubuntu/GMB/COKO/config/
sudo mv /home/ubuntu/app/scripts/static /home/ubuntu/GMB/COKO/
cd /home/ubuntu/GMB/COKO
sudo echo test!
sudo gunicorn --bind 0.0.0.0:8000 config.wsgi:application --daemon