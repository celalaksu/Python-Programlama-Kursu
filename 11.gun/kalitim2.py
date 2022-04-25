# kalıtım - inheritance - Bir sınıfın özelliklerini başka sınıfa aktarma işlemi

# öğrenci - görev - yaptığı iş - kurallar
# öğretmen - branşı - görev
# yönetici - yönetim- öğretmen - meslek

# ortak bilgiler
# kurum - her kişi için aynıdır
# ad - soyad - her kişi için değişen

class Kisi:
    kurum = "MEB"
    def __init__(self,ad,soyad) -> None:
        self.ad = ad
        self.soyad = soyad

    def kuruma_git(self):
        print(f"{self.ad} {self.soyad} kurumuna gider")

class Ogrenci(Kisi):
    gorev = "Öğrenci"
    def __init__(self, ad, soyad) -> None:
        super().__init__(ad, soyad)
        self.sinif = None

class Ogretmen(Kisi):
    gorev = "Öğretmen"
    def __init__(self, ad, soyad) -> None:
        super().__init__(ad, soyad)
        self.brans = None

    def kuruma_git(self):
        print(f"{self.ad} {self.soyad} dersine gider")

class Yonetici(Ogretmen):
    gorev = "Yonetici"
    def __init__(self, ad, soyad) -> None:
        super().__init__(ad, soyad)
        self.yonetici_turu = None
        
    # metod overloading
    def kuruma_git(self):
        super().kuruma_git() # base sınıfta metodun kodlarını çalıştır.
        print("Yönetim işlerini tamamla.")

ogrenci1 = Ogrenci("a","b")

ogretmen1 = Ogretmen("c","d")

yonetici1 = Yonetici("e","f")
yonetici1.kuruma_git()

