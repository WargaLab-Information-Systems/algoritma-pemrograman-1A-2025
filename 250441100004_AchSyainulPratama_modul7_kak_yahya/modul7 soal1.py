def contact_book():
    kontak = {}

    def tambah_kontak(nama, telepon, email):
        if nama in kontak:
            print("Kontak sudah ada.")
            return
        kontak[nama] = [telepon, email]
        print("Kontak berhasil ditambahkan.")

    def lihat_kontak(nama):
        if nama in kontak:
            print(f"Nama: {nama}, Telepon: {kontak[nama][0]}, Email: {kontak[nama][1]}")
        else:
            print("Kontak tidak ditemukan.")

    def ubah_email(nama, email_baru):
        if nama in kontak:
            kontak[nama][1] = email_baru
            print("Email berhasil diubah.")
        else:
            print("Kontak tidak ditemukan.")

    def hapus_kontak(nama):
        if nama in kontak:
            del kontak[nama]
            print("Kontak berhasil dihapus.")
        else:
            print("Kontak tidak ditemukan.")

    while True:
        print("\nMenu:")
        print("1. Tambah Kontak")
        print("2. Lihat Kontak")
        print("3. Ubah Email")
        print("4. Hapus Kontak")
        print("5. Tampilkan Semua Kontak")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            nama = input("Masukkan nama: ")
            telepon = input("Masukkan telepon: ")
            email = input("Masukkan email: ")
            tambah_kontak(nama, telepon, email)
        elif pilihan == '2':
            nama = input("Masukkan nama yang ingin dilihat: ")
            lihat_kontak(nama)
        elif pilihan == '3':
            nama = input("Masukkan nama yang ingin diubah emailnya: ")
            email_baru = input("Masukkan email baru: ")
            ubah_email(nama, email_baru)
        elif pilihan == '4':
            nama = input("Masukkan nama yang ingin dihapus: ")
            hapus_kontak(nama)
        elif pilihan == '5':
            if not kontak:
                print("Tidak ada kontak yang tersimpan.")
            else:
                print("\nDaftar Kontak:")
                for nama, detail in kontak.items():
                    print(f"Nama: {nama}, Telepon: {detail[0]}, Email: {detail[1]}")
        elif pilihan == '6':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

# Inisialisasi program
contact_book()