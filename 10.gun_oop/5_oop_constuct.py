# constructor - yapıcı metot
# gizli olarak bulunan bir yapıdır.
# __init__ metodu otomatik çalışır. Nesne oluşunca 
# self --> sınıftan oluşturulan nesneyi temsil eder.

# class OrnekSinif:
#     ders = "Python"
#     konu = "oop"

#     def __init__(self):
#         print("Yapıcı metod çalıştı.")

# nesne1 = OrnekSinif()
# nesne2 = OrnekSinif()

class OrnekSinif:
    ders = "Python"
    konu = "oop"

    # nesne özelliklleri
    def __init__(self,derssayisi:int):
    
        if derssayisi < 13:
            self.drssys = derssayisi
        else:
            self.drssys = None
        
nesne1 = OrnekSinif(23)
print(nesne1.drssys)
nesne2 = OrnekSinif(5)
print(nesne2.drssys)
        

