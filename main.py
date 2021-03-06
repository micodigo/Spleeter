from flask import Flask, render_template,request,redirect,send_from_directory
import os,shutil

from spleeter.separator import Separator


app = Flask(__name__)

app.config["upload"] = "/media/codelife/Coding Area/Projects/Spleeter/uploads"
@app.route('/',methods=["GET","POST"])
def split():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            stems_seletcted = request.form['stems_select']
            stems='spleeter:'+stems_seletcted+'stems'
            # print(image.filename)
            image.save(os.path.join(app.config["upload"], image.filename))
            separator = Separator(stems)
            # separator = Separator('spleeter:2stems')
            separator.separate_to_file("/media/codelife/Coding Area/Projects/Spleeter/uploads/"+image.filename, '/media/codelife/Coding Area/Projects/Spleeter/files',codec="mp3")
            shutil.make_archive('abc',"zip","files/abc")
            try:
                shutil.move("abc.zip","files")
            except shutil.Error:
                pass
            return send_from_directory("files",path="abc.zip", as_attachment = True)
    return render_template("index.html")


if __name__== '__main__':
    app.run(debug = True)