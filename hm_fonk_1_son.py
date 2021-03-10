
def giris_ekrani():
    print("Hangi işlem?")
    i = 1
    for fonksiyon in fonksiyonlar:
        print(i, "-->", fonksiyon)
        i += 1
    
    print("Seçimini yapınız.")

def veri_girisi():
    sayilar = []
    while True:
        sayi = input("Sayıyı girin (Çıkmak için Ç'ye basın):")
        
        if sayi == "Ç":
            break

        sayi = int(sayi)

        sayilar.append(sayi)
    
    return sayilar

def toplama(a):
    # toplam = sayilar[0] + sayilar[1]
        toplam = 0
        # [30, 40, 60]
        for sayi in a:
            toplam = toplam + sayi

        print(f"Toplama sonucu : {toplam}")

def cikarma(b):
    fark = b[0]
        # 1, 2, 3, 4 .....
    for index in range(1,len(b)):
        fark = fark - b[index] 
    print(f"Çıkarma sonucu : {fark}")

def kullanici_secimi():
    k_secim = input()
    return k_secim

def ana_program():
    while True:
        
        giris_ekrani()

        secim = kullanici_secimi()

        if secim == "Ç":
            break

        if secim not in islemler.keys():
            print("Yanlış giriş yaptın.")
            continue 
        
        sayilar = veri_girisi()

        print(sayilar)

        if secim in islemler.keys():
            islemler[secim](sayilar) # toplama(sayilar)

def carpma(c):
    carpim = 1
    for i in c:
        carpim = carpim * i
    print(f"Çarpma sonucu : {carpim}")

def bolme(b):
    bolunen = b[0]
        # 1, 2, 3, 4 .....
    for index in range(1,len(b)):
        bolunen = bolunen / b[index] 
    print(f"Bölme sonucu : {bolunen}")

islemler = {"1":toplama, "2":cikarma, "3":carpma,"4":bolme}
fonksiyonlar = ["Toplama", "Çıkarma", "Çarpma","Bölme"]

ana_program()