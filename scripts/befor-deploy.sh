#!/bin/bash
if [ -d /app ]; then
    sudo rm -rf /app/
fi
sudo mkdir -vp /app/