import numpy as np

a = np.array([1,2,3,4,5])
type(a)
b = np.array([6,7,8,9,10])
print(a)
ab = a*b
print(ab)

#dtype - veri türü
b = np.array([6,7,8,9,10], dtype=np.float32)
print(b)
print(np.zeros(10,dtype=int))
print(np.ones(5))
print(np.full((3,5),3))

matris_1 = np.full((3,5),3)
print(matris_1)
print(matris_1.ndim) # matrisin boyutu
print(matris_1.shape)# matrisin satır ve sütün sayısı
print(matris_1.size) #eleman sayısı 

# Yeniden şekillendirme ( reshaping )
matris_2 = np.arange(1,28,3) # liste üretir 1 den 30 a kadar 3 er artarak
print(matris_2)
matris_3 = np.arange(1,28,3).reshape((3,3)) # üretilen eleman sayısı
# ile üretilecek matrisin eleman sayısı aynı olmalıdır.
print(matris_3)
print(matris_2.reshape((4,4)))
matris_4 = np.arange(1,17)
print(matris_4.reshape((4,4)))

# matrisleri birleştirme
x = np.array([1,2,3])
y = np.array([4,5,6])
xy = np.concatenate([x,y])
print(xy)
x_l = [1,2,3]
y_l = [1,2,3]
xy_l = x_l + y_l
print(xy_l)


matris_6 = np.array([[1,2,3],[4,5,6]])
birlesik_matris = np.concatenate([matris_6, matris_6])
print(birlesik_matris)
birlesik_matris_2 = np.concatenate([matris_6, matris_6],axis=1)
print(birlesik_matris_2)

# elemanlara erişim - index no kullanılır
print(matris_6[1,2])
print(matris_6)


m_1 = np.arange(20,30)
print(m_1)
print(m_1[0:3])
print(m_1[:3])
print(m_1[5:])

mt_1 = np.random.randint(10, size = (5,5))
print(mt_1)
print(mt_1[0,:])
print(mt_1[0:2,0:3])

# toplu index ile işlem yapma ( fancy index )
d1 = np.arange(0,30,3)
print(d1)
indexler = [1,3,5]
print(d1[indexler])# print(d1[1],d1[3],d1[5])




