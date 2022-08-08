
# kendi kendini çağıran fonksiyonlar - recursive -özyinelemeli

def factorial(n):
    if n == 1:    # The base case (termination condition.)
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4)) # 4 * 3 * 2 * 1 = 24

# 4! 4.3.2.1

def fonk(n):
    sonuc = n * (n-1)
    return sonuc

# 4-- > 4.3 =12

# 2-- > 2.1 = 2

# 12*2 -- 24

sonuc = 1
for i in range(4,0,-1):
    sonuc = i * sonuc
    print(i)
    print(sonuc)


