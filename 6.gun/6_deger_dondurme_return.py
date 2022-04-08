# print("merhaba")# kendisine verilen görevi yerine getirir.

# veri = input("veri gir :")
# kendisine verilen görevi yerine getirir.
# ürettiği / aldığı veriyi programa gönderir.
# değer döndüren fonk.
# return
# input("llll")

def toplama(sayi, sayi2):
    #print(int(sayi) + int(sayi2))
    sonuc = int(sayi) + int(sayi2)
    isim = "Mehmet"
    return sonuc

# fonksiyonun çalışması bittiği anda, fonk. üretilen, tanımlanan bütün veriler yok olur. Ram den silinir.

#toplama(45,67)

gelen_veri=toplama(23,45) # gelen_veri = 68
print(f"fonksiyondan gelen veri {gelen_veri}")
