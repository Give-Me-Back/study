#!/bin/bash
sudo rm -rf /etc/nginx/sites-available/COKO
sudo rm -rf /etc/nginx/sites-enabled/COKO
sudo mv /home/ubuntu/app/scripts/default /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/
sudo systemctl restart nginx

echo 12/13