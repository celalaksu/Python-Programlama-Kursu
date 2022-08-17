# metodları aşırı yükleme - overloading


from typing import overload


class Ornek():
    okul = "arhavi halk eğitim"
    def __init__(self): 
        self.sayi = 0        
        self.adi = "ben"


    def metot_n(self, *args, **kwargs):
        print("Nesnenin parametresiz metodudur.")

        

n1 = Ornek()
n1.fonk()
n1.fonk(56)       


       
