contact = {}

while True :
    print("1. Lihat")
    print("2. Cari")
    print("3. Tambah")
    print("4. Update Email")
    print("5. Hapus")
    print("6. Keluar")
    p = input("pilih menu 1-6: ")

    if p == "1":
        if not contact: print("Belum ada kontak. ")
        for n, v in contact.items(): print(n, "-", v)
    elif p == "2":
        n = input("Nama: ")
        print(contact.get(n, "Kontak tidak ditemukan. "))
    elif p == "3":
        n = input("Nama: ")
        if n in contact:
            print("Nama sudah ada. ")
        else:
            tel = input("Telepon: ")
            mail = input("Email: ")
            contact[n] = [tel, mail]
            print("Kontak ditambah")
    elif p == "4":
        n = input("Nama: ")
        if n not in contact: print("Tidak ditemukan. ")
        else:
            contact[n][1] = input("Email baru: ")
            print("Email diperbarui. ")
    elif p == "5":
        n = input("Nama: ")
        print("Dihapus. " if contact.pop(n, None) else "Tidak ditemukan. ")
    elif p == "6":
        break