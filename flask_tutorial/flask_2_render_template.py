# template dosyaları ( html vs) templates adında bir klasörde olmalıdır.
# aksi halde çalışmaz.

from flask import *
# from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def basic():
    return render_template("flask_2_prerequistes.html")

if __name__ == "__main__":
    app.run()