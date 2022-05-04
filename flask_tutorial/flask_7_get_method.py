from flask import *
# get metodu

app=Flask(__name__)

@app.route("/")


def basic():
        
    return render_template("get_metodu.html")

@app.route("/veriler", methods=["POST","GET"])
def veriler():
    if request.method == "POST":
        name = request.form.get('name')
        password =  request.form["pass"]
        return render_template("veriler.html",name=name, password=password)



if __name__ == "__main__":
    app.run()