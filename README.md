# Minpro-2-DDP-SistemManajemenDataPengunjungPerpustakaan

Nama : Anggitha Christien Wulandari

NIM : 2609116036

Kelas : A

### Deskripsi Singkat program

Sistem Manajemen Data Pengunjung Perpustakaan merupakan program yang digunakan untuk mengelola data pengunjung
perpustakaan. Program ini memiliki fitur login dengan dua role, yaitu admin dan user. Admin 
memiliki akses untuk menambah, melihat, mengubah, dan menghapus data pengunjung. Sedangkan user hanya memiliki
akses untuk melihat data pengunjung. Program menggunakan Dictionary untuk menyimpan data akun, Function untuk membagi program menjadi beberapa bagian, serta beberapa library Python seperti PrettyTable, pwinput, dan datetime.

### Flowchart

<img width="3007" height="2297" alt="Untitled Diagram drawio (7)" src="https://github.com/user-attachments/assets/308acb36-ede4-4648-9258-ca1eeef74e4f" />


### Penjelasan Alur Flowchart
**1. Start dan Menu Utama**

 Proses dimulai dari **Start**, kemudian sistem menampilkan **Menu Utama**. Pada bagian ini pengguna dapat memilih apakah ingin melakukan login ke dalam sistem atau keluar dari program. Menu utama menjadi titik awal sekaligus tempat pengguna kembali setelah menyelesaikan proses tertentu.

 **2. Proses Login**

 Jika pengguna memilih menu **Login**, sistem akan meminta pengguna memasukkan **username dan password**. Data yang dimasukkan kemudian diperiksa oleh sistem untuk memastikan apakah informasi login tersebut sesuai dengan data yang tersimpan.

 **3. Validasi Login**

 Sistem melakukan validasi terhadap username dan password yang dimasukkan. Jika data login salah, sistem akan menampilkan informasi bahwa login tidak berhasil dan pengguna diminta untuk memasukkan kembali username dan password. Jika data login benar, proses dilanjutkan ke pemeriksaan hak akses pengguna.

 **4. Pengecekan Hak Akses**

 Setelah login berhasil, sistem akan menentukan jenis pengguna berdasarkan hak aksesnya. Sistem membedakan pengguna menjadi **Admin** dan **User**. Perbedaan hak akses ini menentukan menu dan fungsi yang dapat digunakan oleh masing-masing pengguna.

 **5. Menu User**

 Jika pengguna teridentifikasi sebagai **User**, sistem akan menampilkan Menu User. Pada menu ini User memiliki akses yang lebih terbatas dibandingkan Admin. User dapat menggunakan fungsi yang telah disediakan, terutama untuk melihat data yang terdapat di dalam sistem.

 **6. Melihat Data oleh User**

 User dapat memilih menu untuk **melihat data**. Sistem kemudian mengambil data yang telah tersimpan dan menampilkannya kepada User. Pada bagian ini User hanya dapat melihat informasi tanpa memiliki kewenangan untuk menambah, mengubah, atau menghapus data.

**7. Logout User**

 Setelah selesai menggunakan sistem, User dapat memilih **Logout**. Sistem akan mengakhiri sesi User dan mengembalikannya ke **Menu Utama**. Setelah kembali ke menu utama, User dapat login kembali atau memilih untuk keluar dari program.

 **8. Menu Admin**

 Jika hasil pemeriksaan hak akses menunjukkan bahwa pengguna adalah **Admin**, sistem akan menampilkan Menu Admin. Admin memiliki hak akses yang lebih lengkap karena dapat melakukan berbagai proses pengelolaan data, seperti menambahkan, melihat, mengubah, dan menghapus data.

 **9. Input Data**

 Pada menu **Input Data**, Admin dapat memasukkan data baru ke dalam sistem. Admin mengisi informasi yang diperlukan sesuai dengan kolom yang tersedia. Setelah data dimasukkan, sistem akan melakukan pemeriksaan untuk memastikan data yang diberikan sudah sesuai dan lengkap.

 **10. Penyimpanan Data**

 Jika data yang dimasukkan sudah sesuai, sistem akan menyimpan data tersebut ke dalam penyimpanan atau database. Data yang berhasil disimpan nantinya dapat ditampilkan kembali melalui menu **Lihat Data**, serta dapat digunakan dalam proses perubahan maupun penghapusan data.

 **11. Lihat Data oleh Admin**

 Admin dapat memilih menu **Lihat Data** untuk melihat seluruh data yang telah tersimpan dalam sistem. Sistem akan mengambil data dari penyimpanan kemudian menampilkannya kepada Admin. Setelah melihat data, Admin dapat kembali ke Menu Admin untuk melakukan proses lainnya.

 **2. Ubah Data**

 Pada menu **Ubah Data**, Admin dapat melakukan perubahan terhadap data yang sudah tersimpan. Admin terlebih dahulu memasukkan identitas data yang ingin diubah, seperti **NIM**. Sistem kemudian mencari data tersebut. Jika data ditemukan, sistem menampilkan data yang bersangkutan sehingga Admin dapat melakukan perubahan terhadap informasi yang diperlukan.

 **13. Validasi Data pada Proses Ubah**

 Sebelum melakukan perubahan, sistem mengecek apakah data berdasarkan identitas yang dimasukkan tersedia. Jika data tidak ditemukan, sistem akan memberikan informasi bahwa data tidak tersedia dan proses perubahan tidak dapat dilakukan. Jika data ditemukan, Admin dapat melanjutkan ke proses perubahan data.

 **14. Update Data**

 Setelah Admin memasukkan informasi baru, sistem akan memperbarui data lama dengan data yang baru. Data yang telah diperbarui kemudian disimpan kembali ke dalam sistem. Dengan demikian, informasi yang sebelumnya tersimpan akan berubah sesuai dengan data terbaru yang diberikan oleh Admin.

 **15. Hapus Data**

 Pada menu **Hapus Data**, Admin dapat menghapus data yang sudah tidak diperlukan. Admin memasukkan identitas data yang ingin dihapus, kemudian sistem melakukan pencarian terhadap data tersebut. Jika data ditemukan, sistem akan melanjutkan proses penghapusan.

 **16. Validasi Data pada Proses Hapus**

 Sistem terlebih dahulu memastikan bahwa data yang ingin dihapus memang tersedia. Jika data tidak ditemukan, sistem memberikan informasi bahwa data tidak tersedia sehingga proses penghapusan tidak dilakukan pengelolaan data. Ketika logout dipilih, sistem akan mengakhiri sesi Admin dan mengembalikan pengguna ke Menu Utama. Admin kemudian dapat melakukan. Jika data ditemukan, sistem dapat melanjutkan ke proses penghapusan.

 **17. Proses Penghapusan Data**

 Setelah data ditemukan, sistem menghapus data tersebut dari penyimpanan. Setelah proses berhasil, sistem memberikan informasi bahwa data telah berhasil dihapus. Admin kemudian dapat kembali ke Menu Admin untuk melakukan proses lainnya.

 **18. Logout Admin**

 Admin dapat memilih **Logout** setelah selesai melakukan pengelolaan data. Ketika logout dipilih, sistem akan mengakhiri sesi Admin dan mengembalikan pengguna ke Menu Utama. Admin kemudian dapat melakukan login kembali atau memilih keluar dari program.

 **19. Keluar dari Sistem**

 Jika pada Menu Utama pengguna memilih **Keluar**, sistem tidak melanjutkan proses lainnya. Sistem akan menampilkan pesan seperti **"Terima Kasih"** sebagai tanda bahwa pengguna telah keluar dari program, kemudian proses akan berakhir pada bagian **End**.

 **20. Kesimpulan Alur**

 Secara keseluruhan, flowchart tersebut menggambarkan sistem yang memiliki **proses login dan pembagian hak akses antara Admin dan User**. User memiliki akses yang lebih terbatas, sedangkan Admin memiliki hak untuk melakukan pengelolaan data berupa **menambah, melihat, mengubah, dan menghapus data**. Setelah menyelesaikan setiap proses, pengguna dapat kembali ke menu utama atau melakukan logout, sedangkan program akan benar-benar berhenti ketika pengguna memilih menu keluar.
