if ("koşul"<"şart"):
    pass # koşul True oldğunda çalışacak
else:
    pass # koşul False oldğunda çalışacak

# kullanıcı adı ve parola


kullanıcı_adı = input("Kullanıcı adınızı giriniz : ")
parola = input("Parolanızı giriniz : ")

# if (kullanıcı_adı=="arhavihem"):
#     if (parola=="12345"):
#         print("Giriş başarılı")
#     else:
#         print("Yanlış giriş yaptınız. Kontrol ediniz! ( iç )")
# else:
#     print("Yanlış giriş yaptınız. Kontrol ediniz! ( dış )")

if (kullanıcı_adı=="arhavihem" and parola=="12345"):
    print("Giriş başarılı")
else:
    print("Yanlış giriş yaptınız. Kontrol ediniz!")