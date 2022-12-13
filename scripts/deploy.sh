#!/bin/bash
sudo rm -rf /etc/nginx/sites-available/*
sudo cp -p /home/ubuntu/app/scripts/COKO /etc/nginx/sites-available/
sudo rm -rf /etc/nginx/sites-enabled/*
sudo ln -s /etc/nginx/sites-available/COKO /etc/nginx/sites-enabled/

sudo systemctl restart nginx

echo 12/13