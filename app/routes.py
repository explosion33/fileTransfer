from flask import render_template, flash, redirect, request, url_for
from werkzeug import secure_filename
from app import app
import os
import logging #change logging status of wekzeug

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

print("KEY:", app.config["KEY"])

#Call to shutdown server and close QR window
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

#main page plus random key handles transfers
@app.route('/' + app.config["KEY"],  methods=['GET', 'POST'])
def upload_file():
    #if there was a POST request
    if request.method == 'POST':
        #get file and gerneate name
        f = request.files['filename']
        filename = secure_filename(f.filename)
        #make sure there was a file if not post Error
        if filename != "":
            #save file and show success page
            pth = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            f.save(pth)
            nicePth = app.config["UPLOAD_FOLDER"] + "/" + str(filename)
            return render_template("success.html", filename=filename, filepath=nicePth, link1=app.config["KEY"])
        else:
            flash("Error: please select a file")

    return render_template('upload.html')

#exit page shutsdown server
@app.route("/exit")
def exit():
    shutdown_server()
    return render_template("exit.html")