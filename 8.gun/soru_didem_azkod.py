liste=[9,5,10,1,4,7,6,8]

for i in range(len(liste)):
    for j in range(len(liste)):
        if j == len(liste)-1:
            break
        if liste[j] > liste[j+1]:
            liste[j], liste[j+1] = liste[j+1], liste[j]

print(liste)