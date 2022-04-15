#!/usr/bin/env bash
# Sets up webservers for deployment: (Run script on both servers)

sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo echo > "Deployment test" /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown $USER:$USER /data/
sudo sed -i "53i\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
