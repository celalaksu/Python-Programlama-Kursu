# recursive - özyinelemeli - kendi kendini çağıran fonksiyon

def faktoriyel(sayi):
    # 5-> 5*4*3*2*1 -> sonuc
    if sayi < 0 :
        return None
    if sayi < 2 :
        return 1

    return sayi * faktoriyel(sayi-1)

print(faktoriyel(5))