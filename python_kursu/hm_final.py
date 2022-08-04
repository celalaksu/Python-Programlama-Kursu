def islem_secenegi():
    islem = input("Hangi işlemi yapacaksınız.( Toplama - 1, Çarpma -2, Çıkarma - 3, Bölme -4, Us alma -5 giriniz ):")
    return islem

def cikis_kontrol():
    devam = input("Çıkış için 'ç' ye basınız.")
    return devam

def veri_girisi():
    sayilar_listesi = []
    while True:
        sayi = input("Veri gir : ")

        kontrol = veri_girisi_kontrolu(sayi)
        print(kontrol)
        print(type(kontrol))
        
        if (kontrol == 1):
            sayi = int(sayi)
            sayilar_listesi.append(sayi)
        else:
            print("Yanlış veri girdiniz")
            continue

        devam = cikis_kontrol()
        print(devam)
        print(type(devam))

        if (devam == "ç"):
            break
    print(sayilar_listesi)
    return sayilar_listesi



def veri_girisi_kontrolu(veri):
    if veri.isdigit():
        return 1
    else:
        return 0
    
        

def toplama(sayilar_listesi):
    if type(sayilar_listesi) == type(list()):
        sonuc = 0
        for i in sayilar_listesi:
            sonuc = sonuc + i
    print(f"Toplama işleminin sonucu {sonuc} tur.")

def cikarma():
    pass

def bolme(sayilar_listesi):
    sonuc = sayilar_listesi[0]
    for i in range(1,len(sayilar_listesi)):
        sonuc = sonuc // sayilar_listesi[i]
    print(f"Bolme işleminin sonucu {sonuc} tur.")

def carpma():
    pass

def us_al():
    pass

def main():
    secenek = islem_secenegi()
    veriler = veri_girisi()
    match secenek:
        case "1":
            toplama(veriler)
        case "2":
            cikarma(veriler)
        case "3":
            carpma(veriler)
        case "4":
            bolme(veriler)
        case "5":
            us_al(veriler)
        case _:
            print("Yanlış seçim yaptınız")

main()
