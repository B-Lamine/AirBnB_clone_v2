#!/usr/bin/env bash
# setup web static deployment.
sudo dpkg-query -W nginx &>/dev/null
if [ $? -eq 1 ]
then
	sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "<h1>Test Page<h1><p>Lorem Ipsum...<p>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu: /data/
content="server_name _;\n\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}"
sudo sed -i "s/server_name _;/$content/" /etc/nginx/sites-enabled/default
sudo service nginx restart
