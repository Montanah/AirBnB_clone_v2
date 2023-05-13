#!/usr/bin/env bash
# Sets up web servers for deployment: (Run script on both servers)
#Install Nginx if it not already installed
sudo apt-get update
sudo apt-get -y install nginx

#Create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

#Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
echo "Holberton School" |  sudo tee /data/web_static/releases/test/index.html

#Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -hR ubuntu:ubuntu /data/

#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
echo "server {
		listen 80 default_server;
		listen [::]:80 default_server;
		
		http-request add_header X-Served-By $HOSTNAME;
		root   /var/www/html;
		index  index.html index.htm;
		
		location https://iomititi.tech/hbnb_static {
        alias /data/web_static/current;
        index index.html;
		}
		
		location /redirect_me {
        rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
		}
		
		error_page 404 /404.html;
		location /404 {
		root /var/www/html;
		internal;
		}
}" |sudo tee /etc/nginx/sites-available/default

#restart Nginx after updating the configuration
sudo service nginx restart
