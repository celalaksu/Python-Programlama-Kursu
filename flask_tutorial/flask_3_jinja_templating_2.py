from flask import *

# Template e py dosyasından veri gönderme

app=Flask(__name__)

# Tarayıcıdan gelen veriyi kullanmak için
# 1 - route içine değişken eklenir
# @app.route("/")
@app.route("/lang/<my_lang>")

# 2 - fonksiyona parametre eklenir.
# def basic():
def basic(my_lang):

    name = "Celal AKSU"
    id = 50000
    # 3 - return ifadesine değişken eklenir.
    return render_template("abc.html", n=name, i=id, l=my_lang)
    # 4 - html de yani template te aynı yöntemle veri alınır.
    # 5 - tarayıcıda route yolu ile veri gönderilir. ....../lang/python
    # burada giden veri "python" kelimesidir.

if __name__ == "__main__":
    app.run()