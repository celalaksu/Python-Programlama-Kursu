# if - Eğer
# Eğer hava soğuksa - mont
# hava sıcaksa - tişort
# if (hava == soğuk): --> -->True, False
#   giyin(mont)

hava = "sıcak"

if (hava == "soğuk"): # True - sıradaki kod çalışır. False - sıradaki kod çalışmaz
    print("tişort giyin") # Satır başındaki boşluk, bu satırın önceki satıra
    # bağlı olarak çalışacağını ifade eder. Yani önceki satır çalışmaz ise
    # girintili satır da çalışmaz.

a = 5
b = 66
# Büyük olan sayı hangisidir?
# Küçük olan sayı hangisidir?
if ( a < b ):
    #print(f"Büyük sayı {b} dir")
    print(f"Küçük sayı {a} dir")

puan = input("Puanını gir : ")
# puan = int(puan)

if (puan >= "50"):
    print("Tebrikler BAŞARDINIZ!") # block - scope
    

print("c"<"d")