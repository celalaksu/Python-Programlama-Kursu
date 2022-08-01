
sayi_1 = input("Birinci sayıyı girin : ") 
sayi_1 = int(sayi_1) 

sayi_2 = input("İkinci sayıyı girin : ")
sayi_2 = int(sayi_2)

islem = input("Hangi işlemi yapacaksınız.( Toplama - 1, Çarpma -2, Çıkarma - 3, Bölme -4 giriniz ):")

if (islem == "1"):
    islem_yazili = "Toplama"
    sonuc = sayi_1 + sayi_2
if (islem == "2"):
    islem_yazili = "Çarpma"
    sonuc = sayi_1 * sayi_2
if (islem == "3"):
    islem_yazili = "Çıkarma"
    sonuc = sayi_1 - sayi_2
if (islem == "4"):
    islem_yazili = "Bölme"
    sonuc = sayi_1 // sayi_2


print(sonuc)
print(f"{islem_yazili} işleminin sonucu {sonuc} dur.") 