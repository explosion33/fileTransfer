import sys, io
import qrcode


# creates a QR image 
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

if __name__ in "main":
    createQR(str(sys.argv[1]), True)


