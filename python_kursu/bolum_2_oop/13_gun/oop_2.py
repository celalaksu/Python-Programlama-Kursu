# Initialize - İlklendirme - init
# Yapıcı metod - constructor
# Nesne --> Sınıfın örneği - class instance

from cgi import print_arguments


class Ornek5:
    pass

class Ornek4():
    pass

class Ornek3(object):
    pass

class Ornek():
    # Sınıf özellikler
    a = 5
    # Yapıcı metod - gizlidir - eklemeseniz bile bulunur
    def __init__(self,sayi): # initialize, nesne tanımlamasını sağlar  - n1 = Ornek()
        # Nesne özellikleri ( self kullanılanlar )
        self.sayi = sayi

        # self - kendi - nesneyi temsil eder

n1 = Ornek(12) # self = n1
print(n1.a)
print(n1.sayi)

n2 = Ornek(15)
print(n2.a)
print(n2.sayi)