# while - verilen koşul sağlandığı ( True ) sürece işlem yap

while "koşul":
    pass # işlemler // kodlar # sonsuz döngü
    # Bir noktada koşulu False yapan bir işlem olmalıdır.
    break

rakam=0
while rakam<10:# rakam 10 dan küçük oluğu sürece
    print(rakam)
    rakam = rakam + 1 # sayma, arttırma

# Başlanğıç Değeri --> Döngüde kontrol edilen değişkenin ilk değeridir.
# Artış Miktarı --> Döngüde kontrol edilen değişkenin artışıdır.
# Bitiş Değeri --> Döngüde kontrol edilen değişkenin son değeridir.
# Koşul

rakam2=9
while rakam2>=0:
    print(rakam2)
    rakam2 = rakam2-1

kontrol_degiskeni=True
while True:
    print("while")
    kontrol_degiskeni = False
    if kontrol_degiskeni==False:
        break