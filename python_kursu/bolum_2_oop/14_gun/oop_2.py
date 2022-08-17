# overriding - eski metodu devre dışı bırakma


class Ornek():
    okul = "arhavi halk eğitim"
    def __init__(self): 
        self.sayi = 0        
        self.adi = "ben"

    def metot_n(self, *args, **kwargs):
        print("Nesnenin parametresiz metodudur.")


class YeniOrnek(Ornek):
    def __init__(self):
        super().__init__()

    def metot_n(self):
        print("Nesnenin parametresiz metodudur. override edilmiş")


n1 = YeniOrnek()
n1.metot_n()      


       
