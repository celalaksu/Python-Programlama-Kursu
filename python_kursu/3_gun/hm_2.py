# toplama programı


sayi_1 = input("Birinci sayıyı girin : ") # Kullanıcı girişinde bütün veriler STRING kabul edilir
# Sayısal veri lazımsa DÖNÜŞTÜRME işlemi yapmalısınız.
# int()
sayi_1 = int(sayi_1) # Kodlar genelde sağdan sola okunur.
# Veri dönüştürülebilir olmalıdır.

sayi_2 = input("İkinci sayıyı girin : ")
sayi_2 = int(sayi_2)

toplam = sayi_1 + sayi_2
print(toplam)
print("Toplama işleminin sonucu : ", toplam)
print(f"Toplama işleminin sonucu {toplam} dur.") # düz metin içine ramdan veri ekleme