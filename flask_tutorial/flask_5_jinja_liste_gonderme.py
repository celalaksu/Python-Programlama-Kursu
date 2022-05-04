from flask import *

# if ve for kullanımı


app=Flask(__name__)

@app.route("/names/<name>")


def basic(name):
   
    a = ["python","java","javascript"]
    return render_template("if_liste.html", n=name, i=id, l=name, q=a)
   

if __name__ == "__main__":
    app.run()