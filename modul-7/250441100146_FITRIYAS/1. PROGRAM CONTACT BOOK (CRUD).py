contacts = {}

def input_angka(pesan):
    while True:
        angka = input(pesan)
        if angka.isdigit():
            return angka
        print("ERROR: Input harus berupa angka!")

def menu_input():
    while True:
        pilih = input("Pilih menu (1-6): ")
        if pilih.isdigit() and 1 <= int(pilih) <= 6:
            return int(pilih)
        print("ERROR: Pilihan harus angka 1-6!")

def tampilkan_kontak():
    if not contacts:
        print("Belum ada kontak.")
    else:
        print("\n=== DAFTAR KONTAK ===")
        for nama, info in contacts.items():
            print(f"Nama: {nama}")
            print(f"Telepon: {info[0]}")
            print(f"Email: {info[1]}")
            print("----------------------")

def cari_kontak():
    nama = input("Masukkan nama kontak yang dicari: ")
    if nama in contacts:
        print(f"Telepon: {contacts[nama][0]}")
        print(f"Email  : {contacts[nama][1]}")
    else:
        print("Kontak tidak ditemukan.")

def tambah_kontak():
    nama = input("Masukkan nama kontak baru: ")
    if nama in contacts:
        print("ERROR: Kontak sudah ada.")
        return
    telepon = input_angka("Masukkan nomor telepon (angka): ")
    if len(telepon) > 13:
        print("ERROR: Nomor telepon tidak boleh lebih dari 13 digit!")
        return

    email = input("Masukkan email: ")
    contacts[nama] = [telepon, email]
    print("Kontak berhasil ditambahkan.")

def update_email():
    nama = input("Masukkan nama kontak yang ingin diperbarui: ")
    if nama not in contacts:
        print("Kontak tidak ditemukan.")
        return
    email_baru = input("Masukkan email baru: ")
    contacts[nama][1] = email_baru
    print("Email berhasil diperbarui.")

def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    if nama in contacts:
        del contacts[nama]
        print("Kontak berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")

while True:
    print("\n=== CONTACT BOOK ===")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak berdasarkan nama")
    print("3. Tambah kontak baru")
    print("4. Perbarui email kontak")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilihan = menu_input()

    if pilihan == 1:
        tampilkan_kontak()
    elif pilihan == 2:
        cari_kontak()
    elif pilihan == 3:
        tambah_kontak()
    elif pilihan == 4:
        update_email()
    elif pilihan == 5:
        hapus_kontak()
    elif pilihan == 6:
        print("Program selesai.")
        break



    