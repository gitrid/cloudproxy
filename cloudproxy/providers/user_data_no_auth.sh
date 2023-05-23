#!/bin/bash
sudo apt-get -y update
sudo apt-get install -y ca-certificates tinyproxy
sudo sed -i 's/Port 8888/Port 8899/g' /etc/tinyproxy/tinyproxy.conf
sudo sed -i '/Allow 127.0.0.1/a Allow ONLYHOSTIP' /etc/tinyproxy/tinyproxy.conf
sudo sed -i 's/#DisableViaHeader Yes/DisableViaHeader Yes/g' /etc/tinyproxy/tinyproxy.conf
sudo systemctl restart tinyproxy
sudo ufw default deny incoming
sudo ufw allow 22/tcp
sudo ufw allow 8899/tcp
sudo ufw --force enable
