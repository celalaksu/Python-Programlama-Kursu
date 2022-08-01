puan = int(input("puan gir"))

# 0-100, 0-50, 50-70, 70-85, 85-100

if (0<=puan<50): # false olduğunda diğer koşullar kontrol edilir.
    print("Başarız")
elif (puan<70):
    print("orta")
elif (puan <85):
    print("İyi")
elif (puan <100):
    print("Pekiyi")
else:
    print("Geçerşiz giriş yaptınız. Kontrol edin!!")