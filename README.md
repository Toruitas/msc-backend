sudo gedit /etc/apache2/ports.conf
 and change listened to 81

sudo gedit mscbackend.conf


<VirtualHost *:81>
        ServerName mscjetson
	WSGIDaemonProcess mscbackend user=jettoruitas group=jettoruitas threads=5
	WSGIScriptAlias / /var/www/mscbackend/app.wsgi
	<Directory /var/www/mscbackend>
		WSGIProcessGroup mscbackend
		WSGIApplicationGroup %{GLOBAL}
		Require all granted
	</Directory>
	ErrorLog /var/www/mscbackend/logs/error.log
</VirtualHost>

sudo iptables -I INPUT -p tcp -m tcp --dport 81 -j ACCEPT
sudo netstat -tnlp | grep :81

