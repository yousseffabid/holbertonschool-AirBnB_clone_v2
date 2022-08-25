#!/usr/bin/env bash
# sets up web servers for the deployment 

sudo apt-get update -y
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo $'<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>' | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -fs /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "s#root\ /var/www/html;#root /var/www/html;\n\tlocation /hbnb_static/{\n\t\talias /data/web_static/current/;\n}#g" /etc/nginx/sites-available/default
sudo service nginx restart
