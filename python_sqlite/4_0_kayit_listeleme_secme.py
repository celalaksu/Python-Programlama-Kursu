import sqlite3
from sqlite3 import Error

# ======= Bağlantının sağlanması

baglanti = None
yol = "veritabani.sqlite"

try:
    baglanti = sqlite3.connect(yol)
    print("Bağlantı başarı ile sağlandı")
except Error as hata:
    print(f"{hata} hatası oluştu.")

# ===============================================

imlec = baglanti.cursor()
musteriler = None

kayitlar_listele = "SELECT * from musteriler"

try:
    imlec.execute(kayitlar_listele)
    musteriler = imlec.fetchall()
except Error as hata:
    print(f"Hata oluştu. {hata} ")

for musteri in musteriler:
    print(musteri)
