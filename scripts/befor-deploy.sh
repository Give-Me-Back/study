#!/bin/bash
if [ -d /opt/app ]; then
    sudo rm -rf /opt/app/
fi
sudo mkdir -vp /opt/app/

echo 2022/12/11 TEST