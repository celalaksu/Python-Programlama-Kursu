from flask import *

# if ve for kullanımı


app=Flask(__name__)

@app.route("/names/<name>")


def basic(name):
   
    return render_template("if_kullanimi.html", n=name, i=id, l=name)
   

if __name__ == "__main__":
    app.run()