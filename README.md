# fileTransfer
transfer files from any device to your computer

## setup

```git clone https://github.com/explosion33/fileTransfer```

if you have ```virtualenviroment``` installed and want to use it run ```setup.bat``` to create virtual enviroment

otherwise run ```pip install -r requiremnts.txt``` to install dependencies

navigate to ```config.py``` and change:

```
PORT:           4 numbers that you want the server to run on
QR_IP:          the ip addesss yoy want encoded into the QR ex:(http://PUBLIC_IP:PORT/) the slash at the end is required
UPLOAD_FOLDER:  the folder you want files to be downloaded to on your computer
```

## start
to start the program run ```start.bat``` or ```startWOenv.bat``` if you arent usinga virtual enviroment
