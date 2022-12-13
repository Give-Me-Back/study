#!/bin/bash
if [ -d /etc/nginx/sites-available/default ]; then
    sudo rm -rf /etc/nginx/sites-available/default
fi
sudo cp -p /home/ubuntu/app/scripts/default /etc/nginx/sites-available/

if [ -d /etc/nginx/sites-enabled/default ]; then
    sudo rm -rf /etc/nginx/sites-enabled/default
fi
sudo ln -s /etc/nginx/sites-available/COKO /etc/nginx/sites-enabled/

sudo systemctl restart nginx

echo 12/13