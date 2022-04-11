# Dökümantasyon - planlama
# Algoritma geliştirme . Farklı programları incelememiz
# Tasarım Desenleri - Design Patterns
# UML - Unified Modelling Language

# hesap mak. - toplama, çıkarma, çarpma, bölme -> fonk
# veriler liste olarak gönderilecek

def toplama(sayilar:list):
    toplam = 0
    for sayi in sayilar:
        toplam = toplam + sayi
        
    print(f"Sayıların toplamı {toplam} 'tır.")

def cikarma(sayilar:list):
    pass

def carpma(sayilar):
    pass

def bolme(sayilar):
    pass

# Kulanıcıyı bilgilendirme
def giris_ekrani():
    print("HESAP MAKİNESİ")
    print("""
    Hangi işlemi yapmak istiyorsunuz?
    1 - Toplama
    2 - Çıkarma
    3 - Çarpma
    4 - Bölme
    5 - Çıkış
    """)

def veri_girisi():
    sayilar = []
    while True:
        sayi = input("Sayı girin: ( Çıkmak için 'Ç'ye basın ) -> ")
        if sayi == "Ç" or sayi == "ç":
            break
        
        if sayi.isnumeric():
            sayi = int(sayi)
            sayilar.append(sayi)
        else:
            print("Yanlış veri girişi yaptınız!")
            continue

    print(sayilar)
    return sayilar

def kullanici_secimi():
    kontrol = "12345"
    while True:
        secim = input("Seçiminizi yapınız : ")
        if secim in kontrol:
            print(secim)
            return secim
        else:
            print("Yanlış seçim yaptınız. Tekrar giriş yapınız : ")
            continue

def ana_program():

    while True:
        giris_ekrani()
        k_secim = kullanici_secimi()

        if k_secim == "5":
            break

        veriler = veri_girisi()
        print(k_secim + " falan")

        match k_secim:
            case "1":
                toplama(veriler)
            case "2":
                cikarma(veriler)
            case "3":
                carpma(veriler)
            case "4":
                bolme(veriler)

ana_program()