from app import app
import qr
import io, sys


if __name__ == '__main__':
    #create a QR code and print to console
    qr.createQR(app.config["QR_IP"] + app.config["KEY"], True)

    #disable text legging from app
    text_trap = io.StringIO()
    sys.stdout = text_trap

    app.run(host="0.0.0.0", port=app.config["PORT"])