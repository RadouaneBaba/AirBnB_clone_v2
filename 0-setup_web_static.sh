#!/usr/bin/env bash
# Setup web server

# install nginx
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/

sudo mkdir /data/web_static/shared/

echo "<html><head></head><body>Hello Airbnb!</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# symbol link

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# give ownership to ubuntu
sudo chown -R ubuntu:ubuntu /data/

# serve /hbnb_static
added_location="\tlocation \/hbnb_static {\n\talias \/data\/web_static\/current\/;}"
sudo sed -i "/server_name _;/a\ $added_location" /etc/nginx/sites-enabled/default

sudo service nginx restart
