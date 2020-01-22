import os
from random import randint

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or ***REMOVED*** # Prevents CSRF attacks
    UPLOAD_FOLDER = "E:/fileShare/files"                                                                            # Where you want files to be downloaded to
    KEY = str(randint(0,1000000000000))                                                                             # random key to prevent access through guessing port
    PORT = 8787                                                                                                     # port to run server on
    QR_IP = ***REMOVED***                                                                      # IP adress + port to run server on (PUBLIC_IP:PORT/)