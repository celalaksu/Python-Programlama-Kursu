# Değişkenler
# Verileri RAM e kayıt etmek için kullanılan yapı
# degişken_adi = veri-değer
from xml.sax.handler import DTDHandler


sayi = 55 # ram de yer ayırıyor, 55 değerini o yere kayıt ediyor. veriye ulaşmak için adres
# adresler okunamaz FF00CC .... değişken adı kullanarak
# int, float, bool, str
sayi = 55 # int - tamsayı
dil = "Python" # str - metinsel - string
durum = True # bool - mantıksal - True False
ondalik_sayi = 10.3 # float - ondalıklı sayı 

# Veri yapıları - Birden fazla veri tutmak

# list - index no --> 0 , 1, 2, ......
listem = [2,4,5, "cisco", 12.34] # ekleme, silme .... - mutable - değiştirilebilir
# liste_adi[index_no]--> elemana erişmek için
# listem[4] # 12.34
# listem[4] = 15 --> elemanı değiştirmek için
# 2 -->index no : 0; 5 -> index no :2 --- // tuple (demet) index no
# tuple
demet = (1,2,"netacad",23.45) # değiştirilemez - unmutable
demet_2 = 1,2,
demet_3 = 1,  # --> demet_3 = (1,)
# demet_adı[index_no] --> elemana erişmek için
# dict - key:value
sozluk = {"ders":"Python", "konu":"Tekrar", "der_sayisi":7, "katilimcilar": ["a","b","c"]}
# "ders", "konu" --> key        "Python", "Tekar" --> verileri - value

# Karar - Kontrol ifadeleri

# if <koşul/lar>:
#       Kodlar --- Koşul True olduğu zaman çalışan kodlar

# if <koşul/lar>:
#       Kodlar --- Koşul True olduğu zaman çalışan kodlar
# else:
#       Kodlar ---- Koşul False olduğu zaman çalışır.

# if (koşul_1 or ( koşul2 and koşul3 )):
#       Kodlar --- Koşul True olduğu zaman çalışan kodlar
# else:
#       Kodlar ---- Koşul False olduğu zaman çalışır.

# if <koşul/lar>:
#       Kodlar --- Koşul True olduğu zaman çalışan kodlar
#       koşul False ise elif e geçer
# elif <koşul>:
#       Kodlar ---- Koşul True olduğu zaman çalışır.
# elif <koşul>:
#       Kodlar ---- Koşul True olduğu zaman çalışır.
# ......
# else:
#       Kodlar. Bütün Koşullar False olduğu zaman çalışır.

# match kontrol_edilecek_degisken:
#       case kontrol_edilecek_değer:
#               kodlar:
#       case kontrol_edilecek_değer:
#               kodlar:
#       case kontrol_edilecek_değer:
#               kodlar:
#       case _:
#               kodlar:


# Döngüler: for, while
# a = 0
# b = 1
# while <koşul>:
#       kodlar -- > Koşul doğru olduğu sürece kodlar tekrar tekrar çalışır.
#                   Koşu false olunca döngü biter
#                   break --> Döngüyü kırmak için kullanılan
#       a = a + 1 ---> Sürekli toplama , arttırma, döngü dışında a nın tanımlanması gerekir
#       a += 1
#       b = b*1 ----> 
# else: --> Döngü çalışmadığı zaman burası çalışır
#   kodlar

# for döngüsü
# for degisken_adı in coklu_veri_içeren_degisken:
#       kodlar ----> coklu_veri_içeren_degisken içindeki her eleman için çalışır.

# coklu_veri_içeren_degisken --> liste, demet, sözlük, range()
# range(10) --> 0 dan 9 a kadar sayılar

# degisken_adı --> Her döngüde coklu_veri_içeren_degisken içindeki bir veriyi tutmak kullanılır
# [2,4,5, "cisco", 12.34] --> 1. döngü de degisken_adı=2
# --> 2. döngü de degisken_adı=4
# --> 3. döngü de degisken_adı=5
# --> 4. döngü de degisken_adı="cisco"
# --> 5. döngü de degisken_adı=12.34

# else:
#     Kodlar -- son eleman üzerinde işlem yapmak. Son eleman üzerinde işlem yapıldığında çalışır

# Fonksiyonlar --> Programı parçalara ayırmak kullanır. 
# Program geliştirme kolaylaşır
# Tekrar kullanma
# hata ayıklama
# Programı genişletmeyi kolaylaştırır

# def fonksiyon_adı(parametre1, parametre2,.......):
#       kodlar
# parametere olmak zorunda değil
# parametre --> Fonksiyonun üzerinde işlme yapması için, fonksiyona gönderilen verileri tutmak için kullanılan değişken
# Kendi kendine çalışmaz, çağrılması geekir.
# fonksiyon_adı(veri1, veri2,.......) --> parantezler olmak zorundadır

# Veri geri döndürme: Fonk. ürettiği veriyi programa geri döndürme işlemi.
# return ile yapılır.

# def fonksiyon_adı(parametre1, parametre2,.......):
#       kodlar
#       return programa_gönderilecek_veri
# geriye veri döndüren fonksiyonlar çağrılırken değişkene atanmalıdır.

# gelen_veri = fonskiyon_adı()


# def fonksiyon_adı(parametre1, parametre2, parametre3="veri"):
#       kodlar
# fonksiyon_adı(p1,p2)
# fonksiyon_adı(p1,p2,p3="giden_veri")
# parametre1, parametre2 -->sıralı arguman- positinal -arguman
# default değeri olan parametreler, sıralı arguman lardan sonra tanımlanır.

# fonksiyon_adı(parametre2="dddd", parametre3="dkdkdkd", parametre2="dkdkdk")

# def int_fonksiyon(p1:int, p2:int):
#     print(p1 + p2)

# # python dinamic typed - veri türlerinin otomatik olarak belirlenen bir dildir.

# int_fonksiyon("6", "6")

# def fonksiyon( p2, p1=43, liste=[2,3,4,] ):
#     pass

# fonksiyon(liste=[5,6,7,], p1= 45)

# fonksiyon(p2=54)

# # SABİT VERİ TÜRLERİ
# SABIT_PI = 3.14,
# type(SABIT_PI)
# # SABİT VERİ TÜRÜNÜ BELİRTMEK İÇİN DEĞİŞKEN ADI büyük harf İLE YAZILIR.
# SABIT_PI_SAYISI = 45
