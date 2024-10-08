# Rast-E
Simple *E-Commerce* app for buy/sell things, even though it can't :P.

## QnAs

### Implementasi *Check-list*
Pembuatan proyek "Rast-E" dimulai dengan pembuatan repo pada Github. Setelah itu, repo tersebut di-*clone* ke local computel. Setelah melakukan *cloning*, maka dilakukan pembuatan project Django

Pertama-tama, pembuatan Virtual Environment (venv) menggunakan `python -m venv <env>` dan diaktifkan menggunakan skrip `activate`. Setelah virtual environtment jadi, melakukan instalasi Django menggunakan `pip`.

Setelah Django berhasil dibuat, maka perlu pembuatan project melalui `django-admin`. Setelah itu, membuat sebuah aplikasi `main` pada project tersebut. Nantinya perlu perubahan pada `main` app dan project agar bisa menampilkan sebuah template yang telah dibuat

### Bagan Django
*N/A: NEED FIX ASAP*

### Fungsi `git`
Dalam pengembangan perangkat lunak, `git` berfungsi sebagai sistem yang melacak sebuah perubahan. Perubahan tersebut akan disimpan dan diidentifikasikan dengan sebuah "version." Git juga bisa digunakan sebagai pembantu kolaborasi sebuah proyek pengembangan perangkat lunak dengan orang lain. Dikarenakan Git selalu menyimpan perubahan tersebut dan diidentifikasikan dengan versi, kita dapat melakukan sebuah "rollback" atau mengubah proyek ke perubahan versi sebelumnya yang berjalan jika perubahan sekarang merusak proyek.

### Django sebagai Framework untuk PBP
Penggunaan Django yang digunakan sebagai framework untuk pembelajaran PBP dipilih dikarenakan pemakaian Django yang simpel. Bahasa pemrograman yang dipakai Django, yaitu Python, dapat dijadikan sebuah alasan dikarenakan bahasanya yang mudah untuk dipahami atau dipelajari, bahkan sudah dipelajari dari mata kuliah Dasar-Dasar Pemrograman 1.

### Model Django yaitu ORM
ORM atau *Object-Relational Mapper* digunakan oleh Django untuk berinteraksi dengan Database. ORM hampir sama dengan SQL Query, dengan layer tambahan dan lebih *pythonic*. Alasan Django menggunakan ORM dibandingkan SQL Query yaitu:
- Pemakaiannya yang mudah. Developer bisa dengan mudah menggunakan ORM dikarenakan mengikuti standar penggunaan Python. Selain itu juga, dapat membantu dengan databse lain yang berbeda sintaks. Developer juga bisa mengatasi error yang akan terjadi.
- Lebih aman. ORM jauh lebih aman daripada SQL Query. Sebuah vulnerability pada SQL yaitu *SQL Injection* yang dapat memasukkan sebuah kueri yang akan dijalankan pada perangkat lunak dari akses luar, misalnya `TextInput` pada field password.
