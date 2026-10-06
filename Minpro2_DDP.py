from prettytable import PrettyTable
import pwinput
from datetime import datetime


# DATA AKUN

akun = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "password": "12345",
        "role": "user"
    }
}


# DATA PENGUNJUNG

data_pengunjung = []


# LOGIN

def login():
    while True:
        print("===== LOGIN PERPUSTAKAAN =====")
        try:
            username = input("Username : ")
            if username == "":
                print("Username tidak boleh kosong!")
                continue
            password = pwinput.pwinput("Password : ")
            if password == "":
                print("Password tidak boleh kosong!")
                continue
            if username in akun:
                if akun[username]["password"] == password:
                    print("Login berhasil!")
                    print("Role :", akun[username]["role"])
                    return akun[username]["role"]
                else:
                    print("Password salah!")
            else:
                print("Username tidak ditemukan!")
        except KeyboardInterrupt:
            print("Jangan klik Ctrl + C!")
        except EOFError:
            print("Jangan klik Ctrl + Z atau Ctrl + D!")


# TAMBAH DATA

def tambah_data():
    print("===== TAMBAH DATA PENGUNJUNG =====")
    #INPUT NAMA
    while True:
        try:
            nama = input("Nama : ")
            if nama == "":
                print("Nama tidak boleh kosong!")
            else:
                break
        except KeyboardInterrupt:
            print("Jangan klik Ctrl + C!")
        except EOFError:
            print("Jangan klik Ctrl + Z atau Ctrl + D!")
    #INPUT NIM
    while True:
        try:
            nim = input("NIM : ")
            if nim == "":
                print("NIM tidak boleh kosong!")
                continue
            ditemukan = False
            for data in data_pengunjung:
                if data[1] == nim:
                    ditemukan = True
                    break
            if ditemukan:
                print("NIM sudah terdaftar!")
            else:
                break
        except KeyboardInterrupt:
            print("Jangan klik Ctrl + C!")
        except EOFError:
            print("Jangan klik Ctrl + Z atau Ctrl + D!")
    #INPUT PRODI
    while True:
        try:
            prodi = input("Prodi : ")
            if prodi == "":
                print("Prodi tidak boleh kosong!")
            else:
                break
        except KeyboardInterrupt:
            print("Jangan klik Ctrl + C!")
        except EOFError:
            print("Jangan klik Ctrl + Z atau Ctrl + D!")
    #INPUT KEPERLUAN
    while True:
        try:
            keperluan = input("Keperluan : ")
            if keperluan == "":
                print("Keperluan tidak boleh kosong!")
            else:
                break
        except KeyboardInterrupt:
            print("Jangan klik Ctrl + C!")
        except EOFError:
            print("Jangan klik Ctrl + Z atau Ctrl + D!")
    #WAKTU KUNJUNGAN
    waktu = datetime.now().strftime("%d-%m-%Y %H:%M")
    data_baru = (
        nama,
        nim,
        prodi,
        keperluan,
        waktu
    )

    data_pengunjung.append(data_baru)

    print("Data pengunjung berhasil ditambahkan!")
    print("Waktu kunjungan :", waktu)


# LIHAT DATA

def lihat_data():
    print("===== DATA PENGUNJUNG =====")
    if data_pengunjung == []:
        print("Belum ada data pengunjung.")
    else:
        tabel = PrettyTable()
        tabel.field_names = [
            "No",
            "Nama",
            "NIM",
            "Prodi",
            "Keperluan",
            "Waktu Kunjungan"
        ]
        nomor = 1
        for data in data_pengunjung:
            tabel.add_row([
                nomor,
                data[0],
                data[1],
                data[2],
                data[3],
                data[4]
            ])
            nomor = nomor + 1
        print(tabel)


# UBAH DATA

def ubah_data():
    print("===== UBAH DATA PENGUNJUNG =====")
    if data_pengunjung == []:
        print("Belum ada data pengunjung.")
        return
    while True:
        try:
            nim = input("Masukkan NIM yang ingin diubah : ")
            if nim == "":
                print("NIM tidak boleh kosong!")
                continue
            ditemukan = False
            posisi = 0
            for data in data_pengunjung:
                if data[1] == nim:
                    ditemukan = True
                    break
                posisi = posisi + 1
            if ditemukan:
                print("Data ditemukan!")
                print("Nama :", data_pengunjung[posisi][0])
                print("NIM :", data_pengunjung[posisi][1])
                print("Prodi :", data_pengunjung[posisi][2])
                print("Keperluan :", data_pengunjung[posisi][3])
                #NAMA BARU
                while True:
                    try:
                        nama_baru = input("Nama baru : ")
                        if nama_baru == "":
                            print("Nama tidak boleh kosong!")
                        else:
                            break
                    except KeyboardInterrupt:
                        print("Jangan klik Ctrl + C!")
                    except EOFError:
                        print("Jangan klik Ctrl + Z atau Ctrl + D!")            
                #NIM BARU
                while True:
                    try:
                        nim_baru = input("NIM baru : ")
                        if nim_baru == "":
                            print("NIM tidak boleh kosong!")
                            continue
                        nim_terpakai = False
                        nomor_data = 0
                        for data in data_pengunjung:
                            if data[1] == nim_baru and nomor_data != posisi:
                                nim_terpakai = True
                                break
                            nomor_data = nomor_data + 1
                        if nim_terpakai:
                            print("NIM sudah digunakan!")
                        else:
                            break
                    except KeyboardInterrupt:
                        print("Jangan klik Ctrl + C!")
                    except EOFError:
                        print("Jangan klik Ctrl + Z atau Ctrl + D!")
                #PRODI BARU
                while True:
                    try:
                        prodi_baru = input("Prodi baru : ")
                        if prodi_baru == "":
                            print("Prodi tidak boleh kosong!")
                        else:
                            break
                    except KeyboardInterrupt:
                        print("Jangan klik Ctrl + C!")
                    except EOFError:
                        print("Jangan klik Ctrl + Z atau Ctrl + D!")
                #KEPERLUAN BARU
                while True:
                    try:
                        keperluan_baru = input("Keperluan baru : ")
                        if keperluan_baru == "":
                            print("Keperluan tidak boleh kosong!")
                        else:
                            break
                    except KeyboardInterrupt:
                        print("Jangan klik Ctrl + C!")
                    except EOFError:
                        print("Jangan klik Ctrl + Z atau Ctrl + D!")
                data_pengunjung[posisi] = (
                    nama_baru,
                    nim_baru,
                    prodi_baru,
                    keperluan_baru,
                    data_pengunjung[posisi][4]
                )
                print("Data berhasil diubah!")
                break
            else:
                print("NIM tidak ditemukan!")
                print("Silakan masukkan NIM kembali.")
        except KeyboardInterrupt:
            print("Jangan klik Ctrl + C!")
        except EOFError:
            print("Jangan klik Ctrl + Z atau Ctrl + D!")


# HAPUS DATA

def hapus_data():
    print("===== HAPUS DATA PENGUNJUNG =====")
    if data_pengunjung == []:
        print("Belum ada data pengunjung.")
        return
    while True:
        try:
            nim = input("Masukkan NIM yang ingin dihapus : ")
            if nim == "":
                print("NIM tidak boleh kosong!")
                continue
            ditemukan = False
            for data in data_pengunjung:
                if data[1] == nim:
                    ditemukan = True
                    break
            if ditemukan:
                print("Data ditemukan!")
                print("Nama :", data[0])
                print("NIM :", data[1])
                print("Prodi :", data[2])
                print("Keperluan :", data[3])
                while True:
                    try:
                        konfirmasi = input(
                            "Yakin ingin menghapus data? (y/n): "
                        )
                        if konfirmasi == "y" or konfirmasi == "Y":
                            data_pengunjung.remove(data)
                            print("Data berhasil dihapus!")
                            break
                        elif konfirmasi == "n" or konfirmasi == "N":
                            print("Penghapusan dibatalkan.")
                            break
                        else:
                            print("Input hanya boleh y atau n.")
                    except KeyboardInterrupt:
                        print("Jangan klik Ctrl + C!")
                    except EOFError:
                        print("Jangan klik Ctrl + Z atau Ctrl + D!")
                break
            else:
                print("NIM tidak ditemukan!")
                print("Silakan masukkan NIM kembali.")
        except KeyboardInterrupt:
            print("Jangan klik Ctrl + C!")
        except EOFError:
            print("Jangan klik Ctrl + Z atau Ctrl + D!")


# MENU ADMIN

def menu_admin():
    while True:
        print("================================")
        print("           MENU ADMIN")
        print("================================")
        print("1. Tambah Data")
        print("2. Lihat Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Logout")
        try:
            pilihan = int(input("Pilih menu 1-5 : "))
            if pilihan == 1:
                tambah_data()
            elif pilihan == 2:
                lihat_data()
            elif pilihan == 3:
                ubah_data()
            elif pilihan == 4:
                hapus_data()
            elif pilihan == 5:
                print("Logout berhasil.")
                break
            else:
                print("Pilihan hanya 1-5!")
        except ValueError:
            print("Input harus berupa angka!")
        except KeyboardInterrupt:
            print("Jangan klik Ctrl + C!")
        except EOFError:
            print("Jangan klik Ctrl + Z atau Ctrl + D!")


# MENU USER

def menu_user():
    while True:
        print("================================")
        print("           MENU USER")
        print("================================")
        print("1. Lihat Data")
        print("2. Logout")
        try:
            pilihan = int(input("Pilih menu 1-2 : "))
            if pilihan == 1:
                lihat_data()
            elif pilihan == 2:
                print("Logout berhasil.")
                break
            else:
                print("Pilihan hanya 1-2!")
        except ValueError:
            print("Input harus berupa angka!")
        except KeyboardInterrupt:
            print("Jangan klik Ctrl + C!")
        except EOFError:
            print("Jangan klik Ctrl + Z atau Ctrl + D!")


# PROGRAM UTAMA

while True:
    print("========================================")
    print(" SISTEM PENDATAAN PENGUNJUNG PERPUSTAKAAN")
    print("========================================")
    print("1. Login")
    print("2. Keluar")
    try:
        pilihan = int(input("Pilih menu 1-2 : "))
        if pilihan == 1:
            role = login()
            if role == "admin":
                menu_admin()
            elif role == "user":
                menu_user()
        elif pilihan == 2:
            print("Program selesai.")
            break
        else:
            print("Pilihan hanya 1-2!")
    except ValueError:
        print("Input harus berupa angka!")
    except KeyboardInterrupt:
        print("Jangan klik Ctrl + C!")
    except EOFError:
        print("Jangan klik Ctrl + Z atau Ctrl + D!")