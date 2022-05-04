from flask import *

# Template e py dosyasından veri gönderme

app=Flask(__name__)

@app.route("/")
def basic():
    name = "Celal AKSU"
    # template dosyasına veri göndermek için n=name kullanıldı.
    # html dosyasında n değişkeni kullanılarak {{n}} şeklinde veriye ulaşılır
    id = 50000
    return render_template("abc.html", n=name, i=id)

if __name__ == "__main__":
    app.run()