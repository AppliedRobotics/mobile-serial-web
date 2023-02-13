systemctl disable mcx-manipulator.service
systemctl stop mcx-manipulator.service
rm /etc/nginx/sites-enabled/mcx.conf

cp -r mobile-serial-web/dist /var/www/mobile-serial/dist

cp mobile.conf /etc/nginx/sites-enabled/
sudo service nginx restart
nginx -s reload

pip3 install -r requirements.txt

cp mobile-server.service /lib/systemd/system/
systemctl daemon-reload
systemctl enable mobile-server.service
systemctl start mobile-server.service
