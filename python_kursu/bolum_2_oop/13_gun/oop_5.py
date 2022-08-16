from ast import Or


class Ornek():
    okul = "arhavi halk eğitim"
    __il__ ="Artvin" # gizli eleman - tam olarak gizli değildir.
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
print(n1.adi)

Ornek.metot_s()
n1.metot_n(10,11)

print(dir(Ornek))
print(Ornek.__il__)

print(hasattr(Ornek(),"okul"))

print(Ornek.__dict__) # sınıfın özelliklerini verir

       
