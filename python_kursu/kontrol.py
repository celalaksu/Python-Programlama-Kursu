def toplama(sayilar_listesi):
    if type(sayilar_listesi) == type(list()):
        sonuc = 0
        for i in sayilar_listesi:
            sonuc = sonuc + i
        print(sonuc)
    else:
        print("Yanlış veri gönderdiniz")

    

toplama([1,2,3,4,5])
        