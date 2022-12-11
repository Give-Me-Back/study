#!/bin/bash
if [ -d /app ]; then
    sudo rm -rf /opt/app/
fi
sudo mkdir -vp /app/

echo 2022/12/11