# KAYNAK : https://realpython.com/python-sql-libraries/#inserting-records

import sqlite3
from sqlite3 import Error

baglanti = None
yol = "veritabani.sqlite"

try:
    baglanti = sqlite3.connect(yol)
    print("Bağlantı başarı ile sağlandı")
except Error as hata:
    print(f"{hata} hatası oluştu.")

