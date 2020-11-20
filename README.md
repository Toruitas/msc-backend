# Msc Thesis Project Main Repository

Msc Creative Computing 2019-2020 Msc Final Thesis Project

By: Stuart Leitch

Supervisor: Mick Grierson

## Table of Contents:
* Companion Repositories
* Installation Instructions
* Introduction
* Project Journal
* Apache notes


## Companion Repositories
1. [Jupyter Notebooks](https://github.com/Toruitas/msc-notebooks)
2. [Backend Server](https://github.com/Toruitas/msc-backend)
3. [Chrome Extension](https://github.com/Toruitas/msc-extension)

## Installation Instructions
### Backend server

Just your typical Python setup - using either venv or Py Poetry. 

Linux/Mac instructions are as follows:
1. `git clone https://github.com/toruitas/msc-backend mscbackend`
2. `cd mscbackend`
3. `python3 -m venv .venv`
4. `source .venv/bin/activate`
5. `pip install -r requirements.txt`
6. Decompress the classifier so that the .pkl file is in the same folder as everything else. `tar -xf final-classifier-2.tar.xz`
7. `export FLASK_app=app.py`
8. `export FLASK_ENV=development`
9. `flask run`
10. Wait a few minutes for the model to load. It will print "Loading machine learning model." in the console.

### Chrome Extension
0. If you're in mscbackend, `cd ..`
1. `https://github.com/Toruitas/msc-extension mscext`
2. `cd mscext`
3. Open Chrome and in the URL bar, navigate to chrome://extensions/
4. In the upper-right corner, enable Developer Mode.
![Dev mode toggle](./Developermode.png)
5. On the new navigation bar that enabling Developer Mode has revealed, click Load unpacked.
6. Find and select the folder `mscext`
7. That's installation complete.

### After installation completes
1. In Chrome, go to (old.reddit.com/r/news)[old.reddit.com/r/news]
2. Wait for a while for the titles to be sent to the Flask server for predictions.
3. See the titles change! Beware these!


### Apache Notes

`sudo gedit /etc/apache2/ports.conf`
 and change `listened` to 81

`sudo gedit mscbackend.conf`


```
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
```

`sudo iptables -I INPUT -p tcp -m tcp --dport 81 -j ACCEPT`

`sudo netstat -tnlp | grep :81`

