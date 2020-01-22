from app import app
import subprocess


if __name__ == '__main__':
    x = subprocess.Popen("python pg.py " + app.config["QR_IP"] + app.config["KEY"], shell=True)
    app.run(host="0.0.0.0", port=app.config["PORT"])