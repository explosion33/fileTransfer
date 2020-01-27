from app import app
import io, sys, os, qrcode, webbrowser, time
from multiprocessing import Process
import subprocess
from winreg import HKEY_CURRENT_USER, OpenKey, QueryValue

def createQR(data, ascii=False):
    """
    createQR(data, ascii): makes a qr code with the given data\n
    data: data to encode (str)
    ascii: weather or not to print to console(bool)\n
    returns PIL img of QR
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(str(data))
    qr.make(fit=True)

    if ascii:
        qr.print_ascii()

    img = qr.make_image(fill_color="black", back_color="white")
    
    return img

def launchBrowser(url):
    #get default browser location

    with OpenKey(HKEY_CURRENT_USER,
                r"Software\Classes\http\shell\open\command") as key:
        cmd = QueryValue(key, None)
    
    num = 0
    end = ""
    for char in cmd:
        if char == '"':
            num += 1
        if num == 2:
            break
        end += char
    loc = end[1::]

    cmd2 = '"' + loc + '"' + " -new-window -url " + url
    time.sleep(0.5)
    p = subprocess.call(cmd2)

    return

if __name__ == '__main__':
    #create a QR code and print to console
    #os.system("cls")
    try:
        mode = sys.argv[1]
    except:
        mode = ""

    if mode == "up":
        createQR(app.config["QR_IP"] + app.config["UPKEY"], True)
        print(app.config["QR_IP"] + app.config["UPKEY"])

        p = Process(target=launchBrowser, args=(app.config["QR_IP"] + app.config["UPKEY"][0:10] + "select",))
        p.start()

    else:
        createQR(app.config["QR_IP"] + app.config["DOWNKEY"], True)
        print(app.config["QR_IP"] + app.config["DOWNKEY"])

    #disable text legging from app
    text_trap = io.StringIO()
    sys.stdout = text_trap


    app.run(host="0.0.0.0", port=app.config["PORT"])