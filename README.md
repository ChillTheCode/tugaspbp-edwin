Tugas 2
Untuk mengimplementasikan checklist tugas Django, saya akan membuat sebuah aplikasi untuk mencari NIKM mahasiswa Fasilkom UI angkatan 2019-2020. Berikut adalah langkah-langkah yang saya lakukan:

1. Membuat proyek Django baru

Saya menggunakan perintah django-admin startproject untuk membuat proyek Django baru dengan nama myproject.

django-admin startproject pbpedwin

2. Membuat aplikasi dengan nama main pada proyek tersebut

Saya menggunakan perintah python manage.py startapp main untuk membuat aplikasi baru dengan nama main.

python manage.py startapp main

3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main
Saya menambahkan routing pada proyek Django untuk menjalankan aplikasi main.

Python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]

4. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.

Saya membuat model baru pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut:

name sebagai nama item dengan tipe CharField.
amount sebagai jumlah item dengan tipe IntegerField.
angkatan sebagai deskripsi item dengan tipe TextField.


from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    angkatan = models.IntegerField()
    description = models.TextField()

5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas .

Saya membuat fungsi baru pada file views.py aplikasi main untuk menampilkan nama aplikasi, nama, dan kelas saya.

Python

from django.shortcuts import render


def show_main(request):
    context = {
        'name': 'Edwin',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

Saya menambahkan routing pada file urls.py aplikasi main untuk memetakan fungsi index() pada views.py.

Python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

//Adaptable error service unavailable
7. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Saya menggunakan perintah python manage.py collectstatic untuk mengumpulkan semua file statis pada aplikasi dan menyimpannya pada direktori staticfiles/.

python manage.py collectstatic
Kemudian, saya menggunakan perintah python manage.py runserver untuk menjalankan aplikasi Django.

python manage.py runserver
Setelah aplikasi Django berjalan, saya dapat mengaksesnya di alamat http://127.0.0.1:8000/.




Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya

![Alt text](image.png)


Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.


MVT adalah singkatan dari Model-View-Template atau seringkali orang mengenalinya dengan nama MTV (Model-Template-View). MVT adalah pola desain atau arsitektur desain yang diikuti Django untuk mengembangkan aplikasi web. Ini sedikit berbeda dari pola desain MVC (Model-View-Controller) yang umum dikenal.

MVT menentukan struktur total dan alur kerja dari aplikasi Django. Dalam arsitektur MVT,
Model pada dasarnya adalah tabel database yang bertugas untuk mengelola data dan diwakili oleh database. View menerima permintaan HTTP dan mengirimkan respons HTTP. Tampilan berinteraksi dengan model dan templat untuk menyelesaikan respons. Template pada dasarnya adalah lapisan front-end dan komponen HTML dinamis dari aplikasi Django.

Perbedaan Utama dengan MVC dan MVVM:
MVT adalah varian dari MVC yang sering digunakan dalam kerangka kerja web seperti Django di Python.



MVC atau Model View Controller adalah sebuah pola desain arsitektur dalam sistem pengembangan website yang terdiri dari tiga bagian yang memiliki peran masing-masing namun saling berkaitan., yaitu: 

Model, bagian yang mengelola dan berhubungan langsung dengan database;
View, bagian yang akan menyajikan tampilan informasi kepada pengguna;
Controller, bagian yang menghubungkan model dan view dalam setiap proses request dari user. Dengan konsep MVC ini, website seakan memiliki bagian yang terpisah dan bisa dikembangkan masing-masing. Maka, proses pembuatan website bisa dilakukan lebih cepat karena developer akan lebih fokus pada pengerjaan salah satu bagian saja. 
Karena dianggap efektif, konsep MVC banyak diterapkan di berbagai framework. Sebagai contoh, di framework PHP terbaik seperti Laravel, CodeIgniter, Symfony, Yii, dan Zend sudah menggunakan konsep ini.

Perbedaan Utama dengan MVT dan MVVM:
MVC adalah pendekatan desain yang umum digunakan di berbagai bahasa pemrograman.
Memisahkan peran masing-masing komponen dengan jelas.



MVVM adalah salah satu arsitektur pembuatan aplikasi berbasis GUI yang berfokus pada pemisahan antara kode untuk logika bisnis dan tampilan aplikasi. Dalam penerapannya, MVVM terbagi atas beberapa layer, yaitu Model, View, dan ViewModel.

Model, Layer ini adalah model atau entitas yang merepresentasikan data yang akan digunakan pada logika bisnis. Umumnya kelas-kelas yang ada di dalamnya berupa POJO atau Plain Old Java Object dan Data Classes jika kita menggunakan Kotlin.
View, tidak seperti layer sebelumnya, layer ini berisi UI dari aplikasi untuk mengatur bagaimana informasi akan ditampilkan. Layer ini akan berisi kelas-kelas, seperti Activity dan Fragment.
ViewModel, Layer yang bertugas untuk berinteraksi dengan model di mana data yang ada akan diteruskan ke layer view.

Perbedaan Utama dengan MVC dan MVT:
MVVM memasukkan ViewModel yang tidak ada di pendekatan lainnya. ViewModel membantu memisahkan logika bisnis dari tampilan dan mengelola state aplikasi dengan lebih efisien.


Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment adalah sebuah wadah untuk menampung pustaka serta modul dalam suatu proyek pekerjaan agar terisolasi. Ketika kita mengerjakan beberapa aplikasi/proyek dengan modul yang sama akan tetapi membutuhkan versi berbeda, disinilah kita membutuhkan virtualenv. Dengan kata lain, Virtual Environment sangat berguna ketika kita membutuhkan dependencies yang berbeda-beda antara project satu dengan lainnya yang berjalan pada satu sistem operasi yang sama

Aplikasi web berbasis Django dapat dibuat tanpa menggunakan virtual environment. Namun, beberapa hal yang perlu diperhatikan jika kita ingin melakukannya:

Jika kita mengembangkan beberapa aplikasi web yang menggunakan versi Python dan paket-paket yang berbeda, dapat terjadi konflik karena aplikasi web kita akan menggunakan versi Python dan paket-paket yang sama dengan sistem operasi kita.

Agar orang lain dapat menjalankan aplikasi web kita, mereka harus memiliki versi Python dan paket-paket yang sama dengan kita. Jika tidak, aplikasi web kita akan lebih sulit untuk dibagikan.

Aplikasi web kita akan menjadi lebih sulit untuk dikelola. Jika kita ingin menginstal paket-paket baru atau memperbarui versi yang sudah ada, kita harus melakukannya dengan hati-hati agar tidak merusak aplikasi web kita.

Secara keseluruhan, penggunaan virtual environment sangat disarankan untuk pengembangan aplikasi web berbasis Django. virtual environment akan membantu kita untuk mengisolasi aplikasi web kita dari aplikasi web lain yang akan mencegah konflik versi Python dan paket-paket. Hal ini mempermudah berbagi aplikasi web kita dengan orang lain karena orang lain hanya perlu memiliki versi Python dan paket-paket yang sama dengan virtual environment kita. Selain itu manfaat dari virtual environment mempermudah pengelolaan aplikasi web kita karena kita dapat menginstal paket-paket baru atau memperbarui versi paket-paket yang sudah ada tanpa khawatir merusak aplikasi web kita.
Kita disarankan untuk menggunakan virtual environment jika kita ingin membuat aplikasi web berbasis Django yang mudah dikelola dan dapat dibagikan dengan orang lain.


Tugas 3

Dalam Django, POST form maupun GET form mengacu pada dua metode berbeda untuk mengirimkan data dari halaman web ke server.

POST Form:

Metode: Data dikirimkan dalam tubuh permintaan HTTP.

Visibilitas: Data tidak terlihat di URL.

Keamanan: Dianggap lebih aman untuk informasi sensitif seperti kata sandi karena data tidak terlihat secara langsung di URL. Namun, ini tidak berarti data terenkripsi. Anda masih harus menggunakan HTTPS untuk komunikasi yang aman.

Ukuran Data: Dapat menangani jumlah data yang besar.

Idempoten: Tidak idempoten, artinya permintaan yang identik dapat memiliki efek yang berbeda.

Penggunaan: Biasanya digunakan saat mengirimkan formulir yang melibatkan informasi sensitif, seperti formulir login, atau saat mengirimkan data yang mungkin mengubah status server.

Penggunaan di Django: Dalam Django, saat Anda mendefinisikan formulir di HTML, biasanya Anda akan menggunakan elemen <form> dengan method="post".


GET Form:

Metode: Data ditambahkan ke URL sebagai parameter kueri.

Visibilitas: Data terlihat di URL.

Keamanan: Kurang aman untuk informasi sensitif karena data terlihat di URL. Hindari menggunakannya untuk kata sandi atau informasi sensitif lainnya.

Ukuran Data: Ada batasan pada jumlah data yang dapat ditangani. URL memiliki batasan panjang maksimum, dan beberapa browser dan server memberlakukan batasan pada panjang URL.

Idempoten: Idempoten, artinya permintaan yang identik akan memiliki efek yang sama.

Penggunaan: Sering digunakan untuk formulir pencarian sederhana, di mana parameter pencarian dapat dienkripsi dalam URL.

Penggunaan di Django: Di Django, Anda menggunakan elemen <form> yang sama di HTML, tetapi dengan method="get".

Pilihan antara menggunakan POST form dan GET form tergantung pada sifat data yang dikirimkan dan persyaratan khusus dari aplikasi Anda. Gunakan POST untuk informasi sensitif dan ketika operasinya tidak idempoten. Gunakan GET untuk operasi di mana parameter dapat dengan mudah dimasukkan dalam URL, seperti pencarian atau penyaringan.



Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data adalah sebagai berikut:

XML (eXtensible Markup Language) adalah format data yang berbasis teks dan dapat dibaca mesin. XML digunakan untuk mendefinisikan struktur data yang kompleks. XML dapat digunakan untuk mengirim berbagai jenis data, termasuk data yang terstruktur, semi-terstruktur, dan tidak terstruktur.

JSON (JavaScript Object Notation) adalah format data yang berbasis teks dan mudah dibaca manusia. JSON digunakan untuk mewakili data dalam bentuk objek dan array. JSON sering digunakan untuk mengirim data dari aplikasi web ke server.

HTML (Hypertext Markup Language) adalah format data yang berbasis teks dan digunakan untuk membuat halaman web. HTML tidak digunakan untuk mengirim data, tetapi dapat digunakan untuk menampilkan data yang dikirim dalam format XML atau JSON.

XML adalah format data yang serbaguna yang dapat digunakan untuk mengirim berbagai jenis data. JSON adalah format data yang mudah dibaca manusia yang sering digunakan untuk mengirim data dari aplikasi web ke server. HTML adalah format data yang digunakan untuk membuat halaman web, tetapi tidak digunakan untuk mengirim data.


JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena beberapa alasan, yaitu:

Kompatibilitas: JSON adalah format data yang populer dan didukung oleh berbagai bahasa pemrograman dan platform.
Kemudahan penggunaan: JSON mudah dibaca dan ditulis oleh manusia, sehingga memudahkan pengembang untuk memahami dan bekerja dengan data yang dipertukarkan.
Kinerja: JSON relatif kecil dan mudah diurai, sehingga tidak membebani jaringan atau server.
Efisiensi: JSON dapat digunakan untuk mewakili berbagai jenis data, termasuk data yang terstruktur, semi-terstruktur, dan tidak terstruktur.

Berikut adalah beberapa contoh penggunaan JSON dalam pertukaran data antara aplikasi web modern:

Mentransfer data dari aplikasi web ke server: JSON sering digunakan untuk mentransfer data dari aplikasi web ke server, seperti data formulir, data pengguna, atau data produk.
Mentransfer data dari server ke aplikasi web: JSON juga sering digunakan untuk mentransfer data dari server ke aplikasi web, seperti data hasil pencarian, data berita, atau data produk.
Mentransfer data antar aplikasi web: JSON dapat digunakan untuk mentransfer data antar aplikasi web, seperti data yang digunakan untuk sinkronisasi data atau untuk berbagi data.

Secara umum, JSON adalah format data yang ideal untuk pertukaran data antara aplikasi web modern. JSON mudah digunakan, efisien, dan kompatibel dengan berbagai bahasa pemrograman dan platform.


Untuk mengimplementasikan checklist tugas Django untuk Implementasi Form dan Data Delivery pada Django, saya mengganti tema website saya yang sebelumnya membuat sebuah aplikasi untuk mencari NIKM mahasiswa Fasilkom UI angkatan 2019-2020, menjadi tempat untuk membeli poster. Berikut adalah langkah-langkah yang saya lakukan:

Langkah 0: Ubah berkas main.html menjadi sesuai yang diinginkan

Langkah 1: Mengatur Routing dari main/ ke /

Buka file urls.py yang ada dalam folder pbpedwin
Ubah path dari main/ menjadi '' pada urlpatterns.
python

Langkah 2: Implementasi Skeleton sebagai Kerangka Views

Buat folder templates di dalam root folder.
Buat file HTML baru bernama base.html di dalam folder templates.
Isi file base.html dengan kode yang diberikan.

Langkah 3: Membuat Form Input Data dan Menampilkan Data Produk Pada HTML

Buat file forms.py di dalam folder main.
Tambahkan kode untuk membuat form ProductForm yang menggunakan model Product.
python
Buka file views.py di dalam folder main.
Tambahkan import yang diperlukan dan buat fungsi create_product.

Langkah 4: Menampilkan Data Produk Pada Halaman Utama

Buka file views.py di dalam folder main.
Ubah fungsi show_main untuk mengambil seluruh objek Product dari database.
python

Langkah 5: Mengembalikan Data dalam Bentuk XML

Buka file views.py di dalam folder main.
Tambahkan import dan buat fungsi show_xml untuk mengembalikan data dalam bentuk XML.

Langkah 6: Mengembalikan Data dalam Bentuk JSON

Buka file views.py di dalam folder main.
Tambahkan import dan buat fungsi show_json untuk mengembalikan data dalam bentuk JSON.

Langkah 7: Mengembalikan Data Berdasarkan ID dalam Bentuk XML dan JSON

Buka file views.py di dalam folder main.
Tambahkan import dan buat fungsi show_xml_by_id dan show_json_by_id untuk mengembalikan data berdasarkan ID dalam bentuk XML dan JSON.

Langkah 8: Penggunaan Postman Sebagai Data Viewer

Pastikan server berjalan dengan perintah python manage.py runserver.
Buka Postman dan buat request GET dengan URL http://localhost:8000/xml atau http://localhost:8000/json untuk menguji pengembalian data.

Langkah 9: Penutup

Pastikan struktur direktori lokal sudah benar.
Lakukan add, commit, dan push untuk memperbarui repositori GitHub.




Lampiran Screenshot Postman

![Alt text](<Screenshot (2016).png>)

![Alt text](<Screenshot (2017).png>)