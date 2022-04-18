from sys import path

#path.append(".\\9.gun\\module\\Extrapack ZIP file.zip") # module klasörü 9.gun klasörü içinde

path.append(".\\module\\Extrapack ZIP file.zip") # module klasörü kök klasörde

# path.append("C:\\........yol....") proje dışındaki paketleri de proje dahil edebilirsiniz.

from extra.iota import FunI

print(FunI())