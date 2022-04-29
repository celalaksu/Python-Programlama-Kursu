from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def _baglantilarTablosuOlustur():
    tabloOlusturSorgusu = QSqlQuery()
    return tabloOlusturSorgusu.exec(
        # çalıştırlabilir sql kodu - sql sorgusu
        # sorgu - query - sql dilinde yazılmış bir koddur.
        # tablo oluşturmak kullanılır.
        # Aşağıdaki sql kodunun açılaması proje notları.txt dosyasında mevcuttur.
        """
        CREATE TABLE IF NOT EXISTS baglantilar (
            kimlik INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            adsoyad VARCHAR(40) NOT NULL,
            meslek VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )

def baglantiOlustur(veritabaniAdi):
    baglanti = QSqlDatabase.addDatabase("QSQLITE")
    baglanti.setDatabaseName(veritabaniAdi)
    baglanti.open()

    if not baglanti.open():
        QMessageBox.warning(
            None,
            "Bağlantılarım",
            f"Veritabanı hatatsı : {baglanti.lastError().text()}",
        )
        return False
    _baglantilarTablosuOlustur()
    return True

