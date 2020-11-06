init_4_nginx = """
#!/bin/bash
apt -y update
apt -y install nginx

#put a default welcome page
mkdir /var/www/ksws_html
echo "<html>
 <body>
   <h1>Welcome to KSWS today!<h1>
 </body>
</html>" > /var/www/ksws_html/index.html

#setup our demo site
echo "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/ksws_html;
    index index.html
    server_name _;
    location / {
        try_files \$uri \$uri/ =404;
    }
}" > /etc/nginx/sites-available/ksws_default

ln -s /etc/nginx/sites-available/ksws_default /etc/nginx/sites-enabled/
rm /etc/nginx/sites-enabled/default

systemctl restart nginx
"""