import imp
from turtle import pen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QWidget,
    QAbstractItemView,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QMessageBox
)

from .model import BaglantilarModeli

class Pencere(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Benim Bağlantılarım")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.baglantiModeli = BaglantilarModeli()
        self.setupUI()

    def setupUI(self):
        # tabloyu oluşturma
        self.tablo = QTableView()
        # tablo yapısını veritabanı tablosu yapısına benzer oluştur 
        self.tablo.setModel(self.baglantiModeli.model)
        self.tablo.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablo.resizeColumnsToContents()
        # buton oluşturma
        self.ekleButonu = QPushButton("YENİ KAYIT")
        self.ekleButonu.clicked.connect(self.eklemePenceresiAc)
        self.silButonu = QPushButton("KAYDI SİL")
        self.silButonu.clicked.connect(self.baglantiyiSil)
        self.hepsiniSilButonu = QPushButton("TÜMÜNÜ SİL")
        self.hepsiniSilButonu.clicked.connect(self.butunKayitlariSil)
        # widgetları ana ekrana ekleme
        buton_layout = QVBoxLayout()
        buton_layout.addWidget(self.ekleButonu)
        buton_layout.addWidget(self.silButonu)
        buton_layout.addStretch()
        buton_layout.addWidget(self.hepsiniSilButonu)
        
        self.layout.addWidget(self.tablo)
        self.layout.addLayout(buton_layout)

    def eklemePenceresiAc(self):
        pencere = KayitEklemePenceresi(self)
        if pencere.exec() == QDialog.Accepted:
            self.baglantiModeli.ekle(pencere.data)
            self.tablo.resizeColumnsToContents()
    
    def baglantiyiSil(self):
        satir = self.tablo.currentIndex().row()
        if satir<0:
            return

        messageKutusu = QMessageBox.warning(
            self,
            "UYARI",
            "Seçilen kaydı silmek istiyor musunuz?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageKutusu == QMessageBox.Ok:
            self.baglantiModeli.sil(satir)

    def butunKayitlariSil(self):
        messageKutusu = QMessageBox.warning(
            self,
            "UYARI",
            "Bütün kayıtları silmek istiyor musunuz?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageKutusu == QMessageBox.Ok:
            self.baglantiModeli.tumunuSil()


class KayitEklemePenceresi(QDialog):
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent=parent)
        self.setWindowTitle("Yeni Bağlantı Ekle")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        # metin kutuları için etiket oluşturma
        self.adsoyadAlani = QLineEdit()
        self.adsoyadAlani.setObjectName("Adınız soyadınız : ")
        self.meslekAlani = QLineEdit()
        self.meslekAlani.setObjectName("Mesleğiniz :")
        self.epostaAlani = QLineEdit()
        self.epostaAlani.setObjectName("Epostanız :")
        # Veri ekleyeceğimiz alanlar ( metin kutuları ) layout oluşturma ve alanları ekleme
        # ve etiketleri metin kutuları ile eşleştirme
        layout = QFormLayout()
        layout.addRow("AdSoyad:", self.adsoyadAlani)
        layout.addRow("Meslek:", self.meslekAlani)
        layout.addRow("Eposta:", self.epostaAlani)
        self.layout.addLayout(layout)

        # Ok ve Cancel standart butonlarının eklenmesi ve 
        # ekle ve vazgec fonksiyonları ile bağlanması
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.ekle)
        self.buttonsBox.rejected.connect(self.vazgec)
        self.layout.addWidget(self.buttonsBox)

    def ekle(self):
        """Verilerin kayıt ekleme penceresi üzerinden alınması"""
        self.data = []
        for field in (self.adsoyadAlani, self.meslekAlani, self.epostaAlani):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "HATA!",
                    f"Bir bağlantı girişi yapmalısınız. {field.objectName()}",
                )
                self.data = None  # Verileri temizle
                return

            self.data.append(field.text())

        if not self.data:
            return

        super().accept()
    
    def vazgec(self):
        super().reject()