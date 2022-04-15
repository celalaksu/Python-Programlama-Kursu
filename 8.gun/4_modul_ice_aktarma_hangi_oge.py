from math import pow , pi

print(pi)

pi = 3.14

print(pi)

print(pow(2,3))

def pow(a,b):
    sonuc = 1
    for x in range(b):
        sonuc = sonuc*a
    print("Fonksiyondan",sonuc)

pow(2,3) # kendi fonk. kullandı