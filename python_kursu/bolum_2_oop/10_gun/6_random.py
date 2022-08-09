# random - rastgele sayı üretmek için kullnaılır
from random import random, seed, randrange, randint # random hem modül adı hemde metotadı

print(random()) # 0.0 - 1.0 arasında değer üretir.

#seed(1) # aynı sayıyı-verileri üretmeniz sağlar

print(random())

print(randrange(10, 100)) # verilen aralıkta sayı üretir

print(randint(0, 100))

from platform import platform # işletim sistemi ile ilgili bilgileri verir

print(platform())
