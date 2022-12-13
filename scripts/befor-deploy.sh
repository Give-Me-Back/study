#!/bin/bash
if [ -d /home/ubuntu/app ]; then
    sudo rm -rf /home/ubuntu/app
fi
sudo mkdir -vp /home/ubuntu/app

echo 2022/12/14