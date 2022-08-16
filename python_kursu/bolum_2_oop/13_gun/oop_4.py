


class Ornek():
    okul = "arhavi halk eğitim"
    def __init__(self): 
        self.sayi = 0        
        self.adi = "ben"

    def metot_s():
        print("bu metod sınıfa aittir")

    def metot_n(self,a,b=15):
        print("nesneye ait metottur", a,b)
        
        
n1 = Ornek()
n1.adi="Celal"
n1.okul="meslek lisesi"
n1.sayi=34
print(n1.adi)

Ornek.metot_s()
n1.metot_n(10,11)


       
