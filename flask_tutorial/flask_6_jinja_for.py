from flask import *

# if ve for kullanımı


app=Flask(__name__)

@app.route("/names")


def basic():
   
    a = ["python","java","javascript"]
    return render_template("for_kullanimi.html",  q=a)
   

if __name__ == "__main__":
    app.run()