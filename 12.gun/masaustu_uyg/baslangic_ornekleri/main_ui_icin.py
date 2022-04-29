import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class Uygulamam(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pencere Adı")
        self.resize(400,200)
        self.centralWidget = QLabel("Merhaba Masaüstü Uygulaması")
        self.setCentralWidget(self.centralWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Uygulamam()
    pencere.show()
    sys.exit(app.exec_())