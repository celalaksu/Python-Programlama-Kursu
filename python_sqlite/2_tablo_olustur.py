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
# Tablo oluşturulması

imlec = baglanti.cursor()

tablo_olusturma_sorgusu = """
CREATE TABLE IF NOT EXISTS musteriler (
id INTEGER PRIMARY KEY AUTOINCREMENT,
isim TEXT NOT NULL,
yas INTEGER,
cinsiyet TEXT
)"""

s2 = """
CREATE TABLE IF NOT EXISTS sehirler (
id INTEGER PRIMARY KEY AUTOINCREMENT,
isim TEXT NOT NULL
)"""

try:
    #imlec.execute(tablo_olusturma_sorgusu)
    imlec.execute(s2)

    baglanti.commit()
    print("Tablo başarıyla oluşturuldu")
except Error as hata:
    print(f"{hata} hatası oluştu.")


