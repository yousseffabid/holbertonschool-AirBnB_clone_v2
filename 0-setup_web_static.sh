#!/usr/bin/env bash
# sets up web servers for the deployment 

sudo apt-get update -y
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo touch /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/current /data/web_static/releases/test/

echo $'<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tWelcome To Holberton\n\t</body>\n</html>' | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo apt-get update -y

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "s#root /var/www/html;#root /var/www/html;\n\tlocation /hbnb_static/{\n\t alias /data/web_static/current/;\n}" /etc/nginx/sites-availabe/default
sudo service nginx restart
