# sözlükler - dictionary - dict

# index YOK
# SIRALI OLMAYAN VERİ YAPISI

# KEY(ANAHTAR)-VALUE(DEĞER) ÇİFTİ ŞEKLİNDEDİR.

# OKUL - ARHAVİHEM, İLÇE - ARHAVİ, DOGTARH - 1990

# VERİLERE ERİŞMEK İÇİN KEY KULLANILIR

sozluk1 = {"adi":"Celal"} # adi = Celal

print(sozluk1)
print(type(sozluk1))

print(sozluk1["adi"]) # sozluk_adı["key"]

szlk2 ={"adi":"Celal", "tcno":12345,"dersler":["a","b","c"]}

print(szlk2["dersler"][1]) # ["a","b","c"]

# farklı veri türleri içirir
# json dosyarının temeli

print(szlk2.items())

print(szlk2.keys())
print(szlk2.values())

for eleman in szlk2.keys():
    print(eleman)

for eleman in szlk2.values():
    print(eleman)

for anahtar, deger in szlk2.items():
    print(f"Key değeri : {anahtar}, valuer değeri : {deger}")

szlk2["adres"] = "bozaiçi mah arhavi"

print(szlk2)

szlk2["adi"] = "Mehmet"
print(szlk2)

del szlk2["adres"]
print(szlk2)

print(szlk2.get("adi"))




