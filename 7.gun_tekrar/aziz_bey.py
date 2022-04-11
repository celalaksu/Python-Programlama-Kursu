def a(b):
    if b<0:
        return None
    if b<2:
        return 1
    return b*a(b-1)  #kendi kendini çağıran fonksiyon örneği


while True:
    c=input("faktöriyeli alıncak sayıyı giriniz yada çıkmak için D tuşuna basınız:" )

    if c == "D" or c== "d":
        break
    
    if c.isnumeric():
        c=int(c)
        print(a(c))
    else:
        print("Yanlış seçim")
        continue