from app import app
import io, sys, os

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


if __name__ == '__main__':
    #create a QR code and print to console
    os.system("cls")

    createQR(app.config["QR_IP"] + app.config["KEY"], True)
    print(app.config["QR_IP"] + app.config["KEY"])
    
    #disable text legging from app
    text_trap = io.StringIO()
    sys.stdout = text_trap

    app.run(host="0.0.0.0", port=app.config["PORT"])