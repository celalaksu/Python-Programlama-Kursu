from ast import Or


class OrnekSinif:
    ders = "Python" # Sınıfın özelliğidir.
    konu = "oop"    # Sınıfın özelliğidir.

    def __init__(self, sayi:int) -> None:
        self.deg1 =""
        self.deg2 = ""
        self.deg3 = ""
        self.sayi = sayi

nesne = OrnekSinif("dkdk")

class deneme:
    x="bir deneme yazılımıdır bu"
    def __init__(self, yas=1):
        self.yas=yas
nesne=deneme()
print(nesne.yas)