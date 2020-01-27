import os
from random import randint

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET KEY' # Prevents CSRF attacks
    UPLOAD_FOLDER = "E:/fileShare/files"                                                                            # Where you want files to be downloaded to
    DOWNKEY = str(randint(0,1000000000000))                                                                         # random key to prevent access through guessing port (for download)
    UPKEY = str(randint(0,1000000000000))                                                                           # random key to prevent access through guessing port (for upload)
    PORT = 8787                                                                                                     # port to run server on
    QR_IP = "http://IP_ADDRESS:" + str(PORT) +"/"                                                                   # IP adress + port to display on qr
    ROOT = os.path.dirname(os.path.abspath(__file__))