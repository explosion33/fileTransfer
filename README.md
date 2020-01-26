# fileTransfer
transfer files from any device to your computer

## setup

```git clone https://github.com/explosion33/fileTransfer```

if you have ```virtualenviroment``` installed and want to use it run ```setup.bat``` to create virtual enviroment

otherwise run ```pip install -r requiremnts.txt``` to install dependencies

navigate to ```config.py``` and change:

```
PORT:           port that you want the server to run on ex: 8080
QR_IP:          the ip addesss yoy want encoded into the QR ex: "http://PUBLIC_IP:" or "http://IPv4:"
UPLOAD_FOLDER:  the folder you want files to be downloaded to on your computer
```

## start
to start the program run ```start.bat``` or ```startWOenv.bat``` if you arent using a virtual enviroment

by default the program runs in download mode, adding ```up``` as an argument runs in upload mode (```down``` also does download mode)

ex: ```start.bat up```
