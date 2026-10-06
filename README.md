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

### Kode Yang Digunakan Dalam Program

**1. import**

Digunakan untuk mengambil library yang dibutuhkan agar program memiliki fitur tambahan.

PrettyTable → menampilkan data pengunjung dalam bentuk tabel agar lebih rapi.

pwinput → menyembunyikan password saat pengguna melakukan login.

datetime → mengambil tanggal dan waktu saat data pengunjung ditambahkan.


**2. def**

Digunakan untuk membuat fungsi, yaitu bagian program yang memiliki tugas tertentu. Dalam program ini digunakan untuk membuat fungsi seperti login, tambah data, lihat data, ubah data, hapus data, menu admin, dan menu user.

**3. if, elif, else**

Digunakan untuk membuat percabangan atau mengambil keputusan berdasarkan kondisi tertentu. Misalnya untuk menentukan pilihan menu, mengecek data, dan menentukan role pengguna.

**4. while**

Digunakan untuk melakukan perulangan selama kondisi masih terpenuhi. Dalam program ini digunakan agar menu dan proses input dapat terus berjalan sampai pengguna memilih untuk keluar atau proses selesai.

**5. for**

Digunakan untuk melakukan perulangan dan memeriksa data satu per satu. Contohnya digunakan untuk mencari apakah NIM sudah terdaftar atau menemukan data berdasarkan NIM.

**6. try-except**

Digunakan untuk menangani kesalahan yang terjadi saat program menerima input dari pengguna. Dengan ini, jika pengguna memasukkan input yang tidak sesuai, program dapat memberikan pesan kesalahan tanpa langsung berhenti.

**7. List**

Digunakan untuk menyimpan banyak data pengunjung dalam satu tempat. Setiap data pengunjung yang ditambahkan akan disimpan ke dalam list data_pengunjung.

**8. Dictionary**

Digunakan untuk menyimpan data akun dalam bentuk pasangan key dan value. Dalam program ini digunakan untuk menyimpan username, password, dan role dari pengguna.

**9. Tuple**

Digunakan untuk menyimpan satu kumpulan data pengunjung yang terdiri dari beberapa informasi, yaitu nama, NIM, prodi, keperluan, dan waktu kunjungan.

**10. append**

Digunakan untuk menambahkan data pengunjung baru ke dalam list. Setelah semua data berhasil diinput dan divalidasi, data tersebut dimasukkan menggunakan append().

**11. remove**

Digunakan untuk menghapus data tertentu dari dalam list. Dalam program ini digunakan ketika admin memilih menu hapus dan data pengunjung berhasil ditemukan.

**12. return**

Digunakan untuk mengembalikan suatu nilai dari sebuah fungsi. Dalam program ini digunakan pada proses login untuk mengembalikan role pengguna, yaitu admin atau user.

**13. break**

Digunakan untuk menghentikan perulangan ketika kondisi tertentu sudah terpenuhi. Misalnya ketika data sudah ditemukan atau pengguna memilih untuk logout dari menu.

**14. Validasi Input**

Digunakan untuk memastikan data yang dimasukkan pengguna sesuai dengan ketentuan program. Contohnya data tidak boleh kosong, NIM tidak boleh sama, pilihan menu harus sesuai, dan konfirmasi hapus hanya menerima y atau n.

**15. Sistem Login dan Role**

Digunakan untuk memeriksa username dan password sebelum pengguna masuk ke sistem. Setelah berhasil login, program membedakan hak akses berdasarkan role. Admin memiliki akses CRUD, sedangkan user hanya dapat melihat data.

**16. CRUD**

Digunakan untuk mengelola data pengunjung. CRUD terdiri dari Create (Tambah), Read (Lihat), Update (Ubah), dan Delete (Hapus). Dalam program ini, fitur CRUD lengkap diberikan kepada admin.

**17. Pencatatan Waktu dengan datetime**

Digunakan untuk mencatat tanggal dan waktu kunjungan secara otomatis ketika data pengunjung ditambahkan. Dengan begitu, setiap data memiliki informasi kapan pengunjung tersebut dicatat.


### Output

**1.Output Menu Utama**

<img width=300 alt="Screenshot 2026-10-06 175118" src="https://github.com/user-attachments/assets/6e5b007e-956c-4ceb-9f59-882731dcda95" />

Pada saat program pertama kali dijalankan, sistem menampilkan Menu Utama sebagai halaman awal program. Menu ini menyediakan dua pilihan utama, yaitu **1. Login**dan **2. Keluar**. Pengguna dapat memilih pilihan sesuai kebutuhan.

**2.Output Login dan Pemilihan Rol**

<img width=300 alt="Screenshot 2026-10-06 175133" src="https://github.com/user-attachments/assets/08021b93-65bd-40ae-a554-d8d95613c689" />

Pada menu login, pengguna diminta memasukkan username dan password. Password dimasukkan menggunakan library pwinput, sehingga karakter password tidak ditampilkan di layar dan tidak terlihat sebagai angka maupun teks. Setelah login berhasil, sistem akan menentukan role pengguna, yaitu admin atau user.

**3.Output Menu Admin**
   
<img width=300 alt="Screenshot 2026-10-06 174451" src="https://github.com/user-attachments/assets/9f934a49-f67c-4ee2-80d8-b2063466020e" />

Setelah berhasil login sebagai admin, program menampilkan Menu Admin yang terdiri dari lima pilihan, yaitu Tambah Data, Lihat Data, Ubah Data, Hapus Data, dan Logout. Admin memiliki akses penuh untuk mengelola data pengunjung.

**4.Pengujian Error Input Huruf**

<img width=300 alt="Screenshot 2026-10-06 174506" src="https://github.com/user-attachments/assets/917fbba6-fae3-4a4f-be45-504809af3a94" />

Pada pengujian ini, dimasukkan input “ABC” pada pilihan menu yang seharusnya berupa angka. Program menangani kesalahan tersebut menggunakan try-except dan menampilkan output “Input harus berupa angka!” sehingga program tetap berjalan dan pengguna dapat memasukkan pilihan kembali.

**5.Pengujian Pilihan Menu yang Tidak Tersedia**

<img width=300 alt="Screenshot 2026-10-06 174646" src="https://github.com/user-attachments/assets/c521ea3e-9b0a-46f7-a295-af891a739f16" />

Pada pengujian berikutnya, dimasukkan angka 7, sedangkan pilihan menu yang tersedia hanya sampai angka 5. Program melakukan validasi dan menampilkan output “Pilihan hanya 1-5!” sehingga pengguna mengetahui bahwa angka tersebut tidak tersedia.

**6.Output Tambah Data Pengunjung**

<img width=300 alt="Screenshot 2026-10-06 174809" src="https://github.com/user-attachments/assets/606ad235-336a-4f1b-8ff0-886749012c10" />

Pada menu Tambah Data, admin diminta memasukkan data pengunjung secara satu per satu, yaitu nama, NIM, prodi, dan keperluan. Setelah seluruh data berhasil diinput dan lolos validasi, program menyimpan data tersebut dan menampilkan output “Data pengunjung berhasil ditambahkan!” serta menampilkan waktu kunjungan secara otomatis.

**7.Output Lihat Data Pengunjung**

<img width="476" height="94" alt="Screenshot 2026-10-06 174916" src="https://github.com/user-attachments/assets/388df767-b78f-45cf-94dd-e50d49956b87" />

Pada pilihan Lihat Data, seluruh data pengunjung yang telah tersimpan ditampilkan menggunakan library PrettyTable. Data ditampilkan dalam bentuk tabel yang berisi No, Nama, NIM, Prodi, Keperluan, dan Waktu Kunjungan, sehingga informasi lebih mudah dibaca.

**8.Output Ubah Data Pengunjung**

<img width=300 alt="Screenshot 2026-10-06 174941" src="https://github.com/user-attachments/assets/e5dcd110-8cdf-42d3-92ef-01ea1699b2a6" />

Pada pilihan Ubah Data, admin terlebih dahulu memasukkan NIM dari data yang ingin diubah. Jika NIM ditemukan, program menampilkan data yang sebelumnya tersimpan dan meminta admin memasukkan nama, NIM, prodi, dan keperluan yang baru. Setelah data diperbarui, program menampilkan output “Data berhasil diubah!”.

**9.Output Lihat Data Setelah Perubahan**

<img width="544" height="95" alt="Screenshot 2026-10-06 175012" src="https://github.com/user-attachments/assets/80e5e0a4-41ed-475d-ae96-f5a12636c131" />

Setelah melakukan perubahan, admin kembali memilih menu Lihat Data untuk memastikan data telah berhasil diperbarui. PrettyTable kemudian menampilkan data pengunjung dengan informasi yang sudah diubah.

**10.Output Logout**

<img width=300 alt="Screenshot 2026-10-06 175219" src="https://github.com/user-attachments/assets/a5268655-74bf-42ac-a114-abba268f9bff" />

Pada pengujian terakhir, admin memilih pilihan 5 yaitu Logout. Program menampilkan output “Logout berhasil.” kemudian mengembalikan pengguna ke Menu Utama, sehingga pengguna dapat login kembali dengan akun lain atau memilih untuk keluar dari program.

**11.Output Login sebagai User**

<img width=300 alt="Screenshot 2026-10-06 175245" src="https://github.com/user-attachments/assets/eb08335f-d666-4d50-985a-88ddaa39bff2" />

Setelah logout dari akun admin, pengguna kembali ke proses login dan memasukkan username serta password untuk akun user. Password tetap disembunyikan menggunakan library pwinput. Setelah data login benar, sistem mengenali role sebagai user dan mengarahkan pengguna ke Menu User.

**12.Output Menu User**

<img width=300 alt="Screenshot 2026-10-06 175327" src="https://github.com/user-attachments/assets/f2d5c70a-3e8d-4b33-9a46-a3691b51736d" />

Setelah berhasil login sebagai user, program menampilkan Menu User yang terdiri dari dua pilihan, yaitu 1. Lihat Data dan 2. Logout. Berbeda dengan admin, user tidak memiliki akses untuk menambah, mengubah, atau menghapus data.

**13.Output Lihat Data sebagai User**

<img width="533" height="94" alt="Screenshot 2026-10-06 175345" src="https://github.com/user-attachments/assets/39f32935-b01f-4d96-8cce-7aa006a4108f" />

Pada Menu User, dipilih pilihan 1 yaitu Lihat Data. Program kemudian menampilkan data pengunjung yang tersimpan dalam bentuk PrettyTable. User hanya dapat melihat data tanpa dapat melakukan perubahan terhadap data tersebut.

**14.Output Logout sebagai User**

<img width=300 alt="Screenshot 2026-10-06 175413" src="https://github.com/user-attachments/assets/04c2a23d-5d50-4c1b-9e6d-9e01ef0dc6d3" />

Setelah selesai melihat data, dipilih pilihan 2 yaitu Logout. Program menampilkan output “Logout berhasil.” kemudian mengembalikan pengguna ke Menu Utama.

**15.Output Hapus Data dan Pembatalan**

<img width=300 alt="Screenshot 2026-10-06 175615" src="https://github.com/user-attachments/assets/e2227f91-3ee8-41f7-854b-3ac188b53496" />

Pengguna kembali login sebagai admin dan memilih pilihan 4 yaitu Hapus Data. Admin diminta memasukkan NIM dari data yang ingin dihapus. Jika NIM ditemukan, program menampilkan pertanyaan “Yakin ingin menghapus data? (y/n)”. Pada pengujian ini dipilih “n”, sehingga program menampilkan output “Penghapusan dibatalkan.” dan data tetap tersimpan.

**16.Output Hapus Data Berhasil**

<img width=300 alt="Screenshot 2026-10-06 175638" src="https://github.com/user-attachments/assets/ae4c5008-1620-4206-8564-ca5994163767" />

Pada percobaan berikutnya, admin kembali memilih menu Hapus Data, memasukkan NIM yang ingin dihapus, kemudian memilih “y” pada konfirmasi penghapusan. Program menjalankan proses penghapusan dan menampilkan output “Data berhasil dihapus!”.

**17.Output Lihat Data Sebagi Admin Setelah Penghapusan**

<img width=300 alt="Screenshot 2026-10-06 175703" src="https://github.com/user-attachments/assets/b0471efe-f75b-43f7-a0a3-57ce7523d8bd" />

Setelah data berhasil dihapus, admin memilih pilihan 2 yaitu Lihat Data untuk memastikan data sudah terhapus. Karena tidak ada lagi data pengunjung yang tersimpan, program menampilkan output “Belum ada data pengunjung.”

**18.Output Lihat Data sebagai User Setelah Data Dihapus**

<img width=300 alt="Screenshot 2026-10-06 175728" src="https://github.com/user-attachments/assets/b1521153-7579-4913-b555-bf311133f0a8" />

Pengguna kemudian logout dari admin dan kembali login sebagai user. Pada Menu User dipilih pilihan 1 yaitu Lihat Data. Karena seluruh data pengunjung sudah dihapus, program juga menampilkan output “Belum ada data pengunjung.” Hal ini menunjukkan bahwa data yang dikelola admin juga dapat dilihat oleh user sesuai hak aksesnya.

**19.Output Program Selesai**

<img width="339" height="121" alt="Screenshot 2026-10-06 175750" src="https://github.com/user-attachments/assets/a50c2f52-cf32-4a71-80ae-d4eb93d3f3f3" />

Setelah selesai melakukan pengujian sebagai user, pengguna memilih Logout dan kembali ke Menu Utama. Kemudian dipilih pilihan 2 yaitu Keluar. Program menampilkan output “Program selesai.” dan proses program berakhir.

**20.Kesimpulan**

Berdasarkan hasil pengujian, Sistem Pendataan Pengunjung Perpustakaan dapat berjalan sesuai dengan fungsi yang telah dirancang. Program berhasil menerapkan proses login dengan role admin dan user, pengelolaan data pengunjung melalui fitur CRUD, serta menampilkan data menggunakan PrettyTable. Selain itu, hasil pengujian juga menunjukkan bahwa validasi input dan error handling dapat bekerja dengan baik, seperti ketika pengguna memasukkan huruf atau pilihan menu yang tidak tersedia. Sistem juga dapat mencatat waktu kunjungan secara otomatis dan memberikan hak akses yang berbeda antara admin dan user.



### Output Lengkap

<img width="544" height="421" alt="Screenshot 2026-10-06 175844" src="https://github.com/user-attachments/assets/abebf989-fe51-4913-8b23-542afbe66f74" />

<img width="539" height="341" alt="Screenshot 2026-10-06 175918" src="https://github.com/user-attachments/assets/f97c1ee9-1bce-4bbb-905e-33c52424ef16" />

<img width="476" height="413" alt="Screenshot 2026-10-06 175957" src="https://github.com/user-attachments/assets/8568a245-c8fa-4a5e-9adc-98d4a4cac67e" />

<img width="536" height="355" alt="Screenshot 2026-10-06 180023" src="https://github.com/user-attachments/assets/c06d4be3-56ec-4501-8d81-20e69ff27316" />

<img width="535" height="353" alt="Screenshot 2026-10-06 180355" src="https://github.com/user-attachments/assets/cfc0a399-a6fb-4049-b74c-12bc1e58220d" />

<img width="532" height="419" alt="Screenshot 2026-10-06 180441" src="https://github.com/user-attachments/assets/83cb6b0d-d42c-4a10-a784-5320195a47b7" />

<img width="537" height="412" alt="Screenshot 2026-10-06 180503" src="https://github.com/user-attachments/assets/bb81ae05-7a62-410c-8282-826bb1234f88" />

<img width="528" height="399" alt="Screenshot 2026-10-06 180527" src="https://github.com/user-attachments/assets/e0857f38-5569-4de6-9aee-f3597737c792" />

<img width="527" height="341" alt="Screenshot 2026-10-06 180552" src="https://github.com/user-attachments/assets/f86162cd-517b-4afb-a0f3-74071974d520" />

<img width="533" height="318" alt="Screenshot 2026-10-06 180613" src="https://github.com/user-attachments/assets/fd038f3b-c23f-4a3c-b9fb-a6fd0c7bca13" />






