# miras - inheritance - kalıtım
# Bir sınıfın özelliklerinin başka bir sınıfa aktarma işlemi

# personel - yönetici - çalışan - müşteri

class personel(): # base class - temel sınıf - üst sınıf - upper sınıf
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad

    def metot_n(self):
        print("nesneye ait",self.ad)


class yonetici(personel):#  türetilmiş sınıf - alt sınıf - sub sınıf
    def __init__(self, ad, soyad):
        super().__init__(ad, soyad)
        self.kidem = ""
        self.a = ""

    def mt_1():
        pass
    

p1 = personel("buse", "özköse")
print(p1.ad)
print(p1.metot_n())

y1 = yonetici("musa","sarı")
print(y1.ad)
print(y1.metot_n())

print(y1.__str__())

    







class calisan:
    pass
class musteri:
    pass
