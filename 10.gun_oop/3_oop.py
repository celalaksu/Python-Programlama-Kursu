class OrnekSinif:
    ders = "Python" # Sınıfın özelliğidir.
    konu = "oop"    # Sınıfın özelliğidir.

    def __init__(self, sayi:int) -> None:
        self.deg1
        self.deg2
        self.deg3
        self.sayi = sayi

    def degisken_yazdir(self):
        print("Öğelerin değerleri",self.ders, self.konu)

nesne1 = OrnekSinif()
print(nesne1.ders, nesne1.konu)
nesne1.degisken_yazdir()

# Değişken - Özellik
# iki tür - 1 - Sınıf Özeliği - Sınıftan üretilen bütün nesneler için ortaktır.
# 2- Nesnenin Özelliği

print("Nesnne2 nin değerleri")
nesne2 = OrnekSinif()
print(nesne2.ders, nesne2.konu)
nesne2.degisken_yazdir()

# Nesne - Sınıfın örneği - instance