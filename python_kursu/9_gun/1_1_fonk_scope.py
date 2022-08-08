y = 45
def fonk2():
    global y # global değişkendir. Bir önceki "y" değişkeni ile aynı değişkendir
    y = 34
    print(y)

fonk2()# 34 yazar
print(y) # 34 yazar
