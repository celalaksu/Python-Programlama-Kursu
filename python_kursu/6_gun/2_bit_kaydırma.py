# <<
# >>
# sayıyı ikilik sayıya dönüştürür. ve bitleri sağa sola kaydırı

a=55
print(bin(a)) # 101  ---> 10

b = a>>1 # bitleri sağa kaydır.
print(bin(b)) # 10  # ikilik sayı sistemindeki karşılığ
print(b)

c = a>>70
print(c)

d = a<<1          # 1010
print(bin(d))
print(d)

# 0,1 -->Makine Dili, bit 
# 01001111  --> Byte ( 8 bit 1 byte)
# 1024 Byte --> 1 KiloByte 
# 1024 KB --> 1 MegaByte
# 1024 MB --> 1 GigaByte
# 1024 GB --> 1 TeraByte

print(hex(a)) # 16
print(oct(a)) # 8 