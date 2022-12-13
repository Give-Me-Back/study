#!/bin/bash
if [ -d /etc/nginx/sites-available/COKO ]; then
    sudo rm -rf /etc/nginx/sites-available/COKO
fi
sudo mv /home/ubuntu/app/scripts/default /etc/nginx/sites-available/

if [ -d /etc/nginx/sites-enabled/COKO ]; then
    sudo rm -rf /etc/nginx/sites-enabled/COKO
fi
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

sudo systemctl restart nginx

echo 12/13