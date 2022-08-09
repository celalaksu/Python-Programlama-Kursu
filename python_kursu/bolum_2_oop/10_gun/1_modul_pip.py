# modül : başkası tarafından geliştirilmiş
# kodları tekrar tekrar kullanmamızı sağlar
# kendimizde modül oluşturabilriz
# her .py dosyası bir modüldür
# içerisinde tek bir konu için oluşturulmuş komutlar( fonksiyon metot değişken) bulunur
# math - matematik ile ilgili işleler

# kullanmak için önce
#   modülü indirmeniz gerekir ( paket )
#   çalışma alanında aktif hale getirmeniz gerekir.

# python ile gelen modüller
# harici olarak yüklenen modüller

# şimdiye kadar kullandığımız komutları içieren modüller
# varsayılan olarak aktif idi

# PYTHON İLE GELENLER

import math # komutları aktif

# komuta ulaşmak için MODÜLAD.KOMUT

print(math.factorial(5))
print(math.sqrt(100))

def sqrt(a):
    return a**(1/2)

print(sqrt(25))
