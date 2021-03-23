class Super():
    def __init__(self, isim):
        self.isim = isim
        self.kalitim = "inheritance"

    def yazdir(self):
        print(self.isim + " sınıfın metodu")

    def __str__(self):
        return "Veri " + self.isim + " nesnesinden gönderildi"

class Sub(Super):
    def __init__(self, isim):
        Super.__init__(self,isim)

    def sub_yazdir():
        pass       

    
nesne1 = Super("super_isim")
print(nesne1.isim)

nesne2 = Sub("sub_isim")
print(nesne2.isim)
print(nesne2.kalitim)

nesne2.yazdir()

print(nesne2)