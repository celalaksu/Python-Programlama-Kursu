# *args, **kwargs

def fonks_1(*args):
    print(args)

fonks_1(1,2,3,4,5,6,7,8)

# tuple - demet 

demet = (1,)
demet2 = 2,
print(demet)
print(type(demet))

demet3 = (12,34,"arhavi",True) # üzerinde ekleme, silme, değiştirme yapılamaz
# Geriye kalan işlemlerde liste kuralları geçerlidir

print(len(demet2))
print(demet3[3])

#demet3[2] = "hopa"

def fonk_2(**kwargs):
    print(kwargs)

fonk_2(a=1,b=2,c=3,d=4,e=5,f=6)