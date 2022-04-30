from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

 # tablo yapısını veritabanı tablosu yapısına benzer oluştur
class BaglantilarModeli:
    def __init__(self) -> None:
        self.model = self._modelOlustur()

    @staticmethod
    def _modelOlustur():
        tabloModeli = QSqlTableModel()
        tabloModeli.setTable("baglantilar")
       # Tablo içinden kaydın güncellenemesini sağlamaktadır. -OnFieldChange
        tabloModeli.setEditStrategy(QSqlTableModel.OnFieldChange)
        tabloModeli.select()

        tablo_basliklari = ("Kimlik", "Ad Soyad", "Meslek", "Eposta")

        for sutunIndex, baslik in enumerate(tablo_basliklari):
            tabloModeli.setHeaderData(sutunIndex, Qt.Horizontal, baslik)

        return tabloModeli

    # Tabloya ekleme işlemi yapar. Burada sql kodları kullanılmamıştır.
    # sql insert yerine PyQt5 in kendi komutları kullanılmıştır.
    def ekle(self, data):
        satirlar = self.model.rowCount()
        self.model.insertRows(satirlar, 1)
        for sutun, alan in enumerate(data):
            self.model.setData(self.model.index(satirlar, sutun + 1),alan)
        self.model.submitAll()
        self.model.select()

    # Tablodan kayıt siler
    def sil(self, satir):
        self.model.removeRow(satir)
        self.model.submitAll()
        self.model.select()

    # Tablodaki kayıtların tümünü siler
    def tumunuSil(self):
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
