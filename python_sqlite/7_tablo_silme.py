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

tablo_sil = "DROP TABLE sehirler"

try:
    imlec.execute(tablo_sil)
    baglanti.commit()
    print("Tablo silindi")
except Error as hata:
    print(f"Hata oluştu. {hata} ")
