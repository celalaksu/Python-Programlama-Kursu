from flask import *

app = Flask(__name__)

@app.route("/hey") # her app route kendinden sonraki fonksiyonu çağırır.
# default route işlemidir. başlangıç sayfası gibi. Farklı bir fonsksiyon yok ise ilk fonksiyonu
# çağırır. / sanra gelen kelime çağırılacak olan fonksiyondur.

def abc():
    return "hi"

@app.route("/")
def hi():
    return "My name is Flask"

@app.route("/mysite/<name>") # sayfaya parametre verme ve fonksiyona aktarma
def name(name):
    return "Hi " + name

# fonsksiyon olmadan if ifadesi çalışmıyor.
if __name__ == '__main__':
    app.run()