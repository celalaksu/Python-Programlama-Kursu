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

kayit_silme = "DELETE FROM musteriler WHERE id = 1"

try:
    imlec.execute(kayit_silme)
    baglanti.commit()
    print("Kayit silindi")
except Error as hata:
    print(f"Hata oluştu. {hata} ")
