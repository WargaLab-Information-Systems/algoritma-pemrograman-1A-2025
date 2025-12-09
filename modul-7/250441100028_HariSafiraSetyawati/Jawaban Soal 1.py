# Program Contact Book dengan CRUD

contacts = {}

def tampilkan_semua():
    if not contacts:
        print("\nBelum ada kontak yang tersimpan.\n")
    else:
        print("\n=== Daftar Semua Kontak ===")
        for nama, info in contacts.items():
            print(f"Nama : {nama}")
            print(f"Telepon : {info[0]}")
            print(f"Email : {info[1]}")
            print("-" * 30)
        print()

def cari_kontak():
    nama = input("Masukkan nama yang ingin dicari: ")
    if nama in contacts:
        print("\nKontak ditemukan:")
        print(f"Nama : {nama}")
        print(f"Telepon : {contacts[nama][0]}")
        print(f"Email : {contacts[nama][1]}\n")
    else:
        print("\nKontak tidak ditemukan!\n")

def tambah_kontak():
    nama = input("Masukkan nama kontak baru: ")
    if nama in contacts:
        print("Kontak dengan nama tersebut sudah ada.\n")
        return
    telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")
    contacts[nama] = [telepon, email]
    print("Kontak berhasil ditambahkan!\n")

def update_email():
    nama = input("Masukkan nama kontak yang ingin diperbarui emailnya: ")
    if nama in contacts:
        email_baru = input("Masukkan email baru: ")
        contacts[nama][1] = email_baru
        print("Email berhasil diperbarui!\n")
    else:
        print("Kontak tidak ditemukan!\n")

def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    if nama in contacts:
        del contacts[nama]
        print("Kontak berhasil dihapus!\n")
    else:
        print("Kontak tidak ditemukan!\n")

# Menu Utama
while True:
    print("=== CONTACT BOOK MENU ===")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak")
    print("4. Perbarui email kontak")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_semua()
    elif pilihan == "2":
        cari_kontak()
    elif pilihan == "3":
        tambah_kontak()
    elif pilihan == "4":
        update_email()
    elif pilihan == "5":
        hapus_kontak()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.\n")