#!/bin/bash
sudo rm -rf /etc/nginx/sites-available/COKO
sudo mv /home/ubuntu/app/scripts/COKO /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/COKO /etc/nginx/sites-enabled
sudo systemctl restart nginx
echo 2022/12/11