# Birden yüze kadar, tek sayıların toplamı kaçtır.
toplam = 0

for tek_sayi in range(1,100,2):
    toplam = toplam + tek_sayi
    if tek_sayi == 11:
        break
else:
    print("Döngü bitti.")

print(f"Tek sayilarin toplamı: {toplam}")



