# fonk veri üretir ( veriyi saklayamaz )
# fonk ürettiği veriyi geri döndürmemiz gerekir. veri lazımsa
# rama kayıt edilmesi gerekir.

#veri = input("veri gir")

# return --> Fonksiyon daki veriyi geri döndürür.

# Veriyi geri döndüren fonksiyonlar

def carpma(a,b,c):
    sonuc = a*b*c
    return sonuc

carpma_sonucu = carpma(3,4,5)
print(carpma_sonucu)