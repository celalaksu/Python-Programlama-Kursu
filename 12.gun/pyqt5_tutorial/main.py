import sys
from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.uic import loadUi
from main_window_ui import Ui_MainWindow

class MyApp(QWidget,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec())