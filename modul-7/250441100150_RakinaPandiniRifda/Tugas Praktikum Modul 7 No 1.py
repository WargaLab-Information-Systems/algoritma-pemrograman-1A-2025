# Membuat contact book dengan fitur CRUD 
def input_menu():
    while True:
        try:
            pilihan = int(input("Pilih menu (1-6): "))
            if 1 <= pilihan <= 6:
                return pilihan
            else:
                print("Pilihan harus antara 1 sampai 6!")
        except ValueError:
            print("Input harus berupa angka! Coba lagi.")

def input_nomor():
    while True:
        nomor = input("Masukkan nomor telepon: ")
        try:
            int(nomor)
            return nomor
        except ValueError:
            print("Nomor telepon hanya boleh angka! Coba lagi.")

def input_nama(pesan):
    while True:
        nama = input(pesan)
        try:
            int(nama)
            print("Nama tidak boleh berupa angka! Coba lagi.")
        except ValueError:
            if nama == "":
                print("Nama tidak boleh kosong!")
            else:
                return nama
            
#read
def tampilkan_kontak(kontak):
    if not kontak:
        print("Tidak ada kontak yang tersedia.")
        return
    print("Daftar Kontak:")
    for nama, info in kontak.items():
        print(f"Nama : {nama}")
        print(f"Telepon : {info[0]}")
        print(f"Email : {info[1]}")
        print("-" * 40)

#read
def cari_kontak(kontak):
    nama = input_nama("Masukkan nama kontak yang dicari: ")
    if nama in kontak:
        print("Kontak ditemukan:")
        print(f"Nama : {nama}")
        print(f"Telepon : {kontak[nama][0]}")
        print(f"Email : {kontak[nama][1]}")
    else:
        print("Kontak tidak ditemukan.")

#create
def tambah_kontak(kontak):
    nama = input_nama("Masukkan nama kontak baru: ")
    if nama in kontak:
        print("Kontak sudah ada!")
        return
    telepon = input_nomor()
    email = input("Masukkan email: ")
    kontak[nama] = [telepon, email]
    print("Kontak berhasil ditambahkan.")

#update
def update_email(kontak):
    nama = input_nama("Masukkan nama kontak yang ingin diperbarui emailnya: ")
    if nama not in kontak:
        print("Kontak tidak ditemukan.")
        return
    email_baru = input("Masukkan email baru: ")
    kontak[nama][1] = email_baru
    print("Email berhasil diperbarui.")

#delete
def hapus_kontak(kontak):
    nama = input_nama("Masukkan nama kontak yang ingin dihapus: ")
    if nama not in kontak:
        print("Kontak tidak ditemukan.")
        return
    del kontak[nama]
    print("Kontak berhasil dihapus.")

kontak = {}

while True:
    print("=== Menu Contact Book ===")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak")
    print("4. Update email kontak")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilihan = input_menu()

    if pilihan == 1:
        tampilkan_kontak(kontak)
    elif pilihan == 2:
        cari_kontak(kontak)
    elif pilihan == 3:
        tambah_kontak(kontak)
    elif pilihan == 4:
        update_email(kontak)
    elif pilihan == 5:
        hapus_kontak(kontak)
    elif pilihan == 6:
        print("Terima kasih! Program selesai.")
        break