import sys


from PyQt5.QtWidgets import QApplication

from .database import baglantiOlustur
from .views import Pencere

def main():
    uygulama = QApplication(sys.argv)
    # Veritabanı bağlantısı
    if not baglantiOlustur("baglantilarim.sqlite"):
        sys.exit(1)

    pencere =  Pencere()
    pencere.show()
    sys.exit(uygulama.exec())
