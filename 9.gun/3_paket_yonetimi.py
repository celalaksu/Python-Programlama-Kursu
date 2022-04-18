"""
pip -> paket yönetimi
Kurulum
pip install paket_adı ( python sürümü ile uyumlumu?)
pip install paket_adı == "paket version "

Linux
pip -> python2
pip3 ->pyhton3

Güncelleme
pip install -U paket_adı

Kaldırma
pip uninstall paket_adı

Yardım
pip help

Kurulu paketler
pip list

pip özellikleri
pip show pip

" ADD TO PATH " KURULUM YAPARKEN

"BAĞIMLILIKLAR "
Bir paket geliştirilirken, başka paketler kullanılmış olabilir.
Kullanılan paketlere Bağımlı paketler.
Bir paket-> birden fazla paket kurulur.

Meb hattı için pip ayarları
ı. yol - cmd komut satırından yazın.

pip config  --global set global.cert "C:\MEB_SERTIFIKASI.crt"
pip config  --global set global.trusted-host "files.pthonhosted.org pypi.org"

II. yol
C:\ProgramData\pip\pip.ini		dosyasına aşağıdaki kodları ekleyin.

[global]
cert = C:\MEB_SERTIFIKASI.crt
trusted-host = files.pythonhosted.org pypi.org

"""
