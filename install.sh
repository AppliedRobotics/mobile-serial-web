systemctl disable mcx-manipulator.service
systemctl stop mcx-manipulator.service

cp -r mobile-serial-web/dist /var/www/mobile-serial

cp mobile.conf /etc/nginx/sites-enabled/
nginx -s reload

pip3 install -r requirements.txt

cp mobile-server.service /lib/systemd/system/
systemctl daemon-reload
systemctl enable mobile-server.service
systemctl start mobile-server.service