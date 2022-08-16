# hata üretme
# raise - herhangi bir yerde manuel hata oluşturmak için kullanılır.

# raise ZeroDivisionError

# assert koşul --> bir koşul gerçekleşmediğinde hata üretir

import math

x = float(input("Enter a number: "))
try:
    assert x >= 0.0
except:
    print("Hata oluştu")

x = math.sqrt(x)

print(x)