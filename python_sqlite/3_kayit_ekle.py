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

sehir_ekle = """
INSERT INTO
  sehirler (isim)
VALUES
  ('Artvin')"""

kullanici_ekle = """
INSERT INTO
  musteriler (sehirid, isim, soyidim)
VALUES
  (1, "Kerem", "Uzuner");
"""
try:
    imlec.execute(sehir_ekle)
    imlec.execute(kullanici_ekle)
    baglanti.commit()
    print("Kayıt başarı ile eklendi.")
except Error as hata:
    print(f"{hata} hatası oluştu.")