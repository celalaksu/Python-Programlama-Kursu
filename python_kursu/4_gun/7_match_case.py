# match degisken:
#   case degisken_değeri:
#       kodlar
#   case degisken_değeri2:
#       kodlar
#   ........ ( değişkenin sahip olacabileceği değerler kadar)
#   case_: ( kontrol edilen değerler dışında bir değer ile karşılaşınca çalışır)
#       kodlar 

sayi_1 = input("Birinci sayıyı girin : ") 
sayi_1 = int(sayi_1) 

sayi_2 = input("İkinci sayıyı girin : ")
sayi_2 = int(sayi_2)

islem = input("Hangi işlemi yapacaksınız.( Toplama - 1, Çarpma -2, Çıkarma - 3, Bölme -4 giriniz ):")

match islem:
    case "1":
        islem_yazili = "Toplama"
        sonuc = sayi_1 + sayi_2
    case "2":
        islem_yazili = "Çarpma"
        sonuc = sayi_1 * sayi_2
    case "3":
        islem_yazili = "Çıkarma"
        sonuc = sayi_1 - sayi_2
    case "4":
        islem_yazili = "Bölme"
        sonuc = sayi_1 // sayi_2
    case _:
        print("Yanlış seçim yaptınız.")

print(sonuc)
print(f"{islem_yazili} işleminin sonucu {sonuc} dur.") 