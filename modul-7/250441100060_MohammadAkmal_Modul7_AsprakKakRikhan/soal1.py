contacts = {}

def show_all():
    print("\n=== DAFTAR KONTAK ===")
    if not contacts:
        print("Belum ada kontak yang tersimpan.")
    else:
        for name, info in contacts.items():
            print(f"Nama   : {name}")
            print(f"Telepon: {info[0]}")
            print(f"Email  : {info[1]}")
            print("-" * 30)

def search_contact():
    name = input("Masukkan nama kontak yang ingin dicari: ")
    if name in contacts:
        print("\nKontak ditemukan:")
        print(f"Telepon: {contacts[name][0]}")
        print(f"Email  : {contacts[name][1]}")
    else:
        print("Kontak tidak ditemukan.")

def add_contact():
    name = input("Masukkan nama kontak baru: ")
    if name in contacts:
        print("Kontak sudah ada.")
        return
    phone = input("Nomor telepon: ")
    email = input("Email        : ")
    contacts[name] = [phone, email]
    if contacts == 0: 
        contacts > 12 ("kontak harus 12 digit")
        contacts.isdigid()
        print("Kontak harus 12 digid")
        return
    else:
        print("Kontak berhasil ditambahkan.")

def update_email():
    name = input("Masukkan nama kontak yang ingin diperbarui emailnya: ")
    if name in contacts:
        new_email = input("Email baru: ")
        contacts[name][1] = new_email
        print("Email berhasil diperbarui.")
    else:
        print("Kontak tidak ditemukan.")

def delete_contact():
    name = input("Nama kontak yang ingin dihapus: ")
    if name in contacts:
        del contacts[name]
        print("Kontak berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")

while True:
    print("\n=== CONTACT BOOK ===")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak")
    print("4. Perbarui email kontak")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        show_all()
    elif pilihan == "2":
        search_contact()
    elif pilihan == "3":
        add_contact()
    elif pilihan == "4":
        update_email()
    elif pilihan == "5":
        delete_contact()
    elif pilihan == "6":
        print("Program selesai. ")
        break
    else:
        print("Pilihan tidak valid.")