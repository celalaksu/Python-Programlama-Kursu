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

kayit_guncelle = """UPDATE musteriler SET isim = 'Karasu' WHERE id = 2"""

try:
    imlec.execute(kayit_guncelle)
    baglanti.commit()
    print("Kayit güncellendi")
except Error as hata:
    print(f"Hata oluştu. {hata} ")
