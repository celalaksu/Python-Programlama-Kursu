dosya = open("dosya.txt","a",encoding='utf-8')

dosya.write("Birinci satır\n")
dosya.write("İkinci satır\n")

satirlar = ["Üçüncü satır\n","Dördüncü satır\n","Beşinci satır\n"]
dosya.writelines(satirlar)

dosya.close()