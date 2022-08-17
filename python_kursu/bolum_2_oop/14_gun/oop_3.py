# Çokbiçimlilik - Polymorphism


class Ornek(object):
    okul = "arhavi halk eğitim"
    def __init__(self): 
        self.sayi = 0        
        self.adi = "ben"

    def metot_n(self):
        print("Nesnenin parametresiz metodudur.", self.adi)


class YeniOrnek(Ornek):
    def __init__(self):
        super().__init__()

   


n1 = Ornek()
n1.adi = "Mehmet"
n1.metot_n()   

n2 = YeniOrnek()
n2.adi = "Ayşe"
n2.metot_n()


       
