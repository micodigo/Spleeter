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
            print(image.filename)
            image.save(os.path.join(app.config["upload"], image.filename))

            separator = Separator('spleeter:4stems')
            separator.separate_to_file("/media/codelife/Coding Area/Projects/Spleeter/uploads/abc.mp3", '/media/codelife/Coding Area/Projects/Spleeter/files',codec="mp3")
            shutil.make_archive('abc',"zip","files/abc")
            try:
                shutil.move("abc.zip","files")
            except shutil.Error:
                pass
            return send_from_directory("files",path="abc.zip", as_attachment = True)
            return redirect(request.url)
    return render_template("index.html")


if __name__== '__main__':
    app.run(debug = True)