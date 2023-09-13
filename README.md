
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


