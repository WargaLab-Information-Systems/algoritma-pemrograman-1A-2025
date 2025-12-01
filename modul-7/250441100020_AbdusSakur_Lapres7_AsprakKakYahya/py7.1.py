def main():
    kontak = {
        "agus": ["08123456789", "agus@gmail.com"]
    }

    while True:
        print("1. Tampilkan Semua Kontak")
        print("2. Cari Kontak")
        print("3. Tambah Kontak")
        print("4. Update Email Kontak")
        print("5. Hapus Kontak")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            if not kontak:
                print("Belum ada data kontak.")
            else:
                print("Daftar Kontak:")
                for nama, data in kontak.items():
                    print(f"- {nama}: Telp={data[0]}, Email={data[1]}")

        elif pilihan == "2":
            nama = input("Masukkan nama kontak: ").lower()
            if nama in kontak:
                print(f"Data ditemukan: Telp={kontak[nama][0]}, Email={kontak[nama][1]}")
            else:
                print("Kontak tidak ditemukan.")

        elif pilihan == "3":
            while True:
                nama = input("Nama: ").lower()
                if nama in kontak:
                    print("Nama ini sudah ada! Gunakan nama lain.")
                else:
                    break

            while True:
                telp = input("Nomor telepon: ")
                if any(telp == data[0] for data in kontak.values()):
                    print("Nomor telepon ini sudah terdaftar! Masukkan nomor lain.")
                else:
                    break

            while True:
                email = input("Email: ")
                if any(email == data[1] for data in kontak.values()):
                    print("Email ini sudah terdaftar! Masukkan email lain.")
                else:
                    break
            kontak[nama] = [telp, email]
            print("Kontak berhasil ditambahkan.")

        elif pilihan == "4":
            nama = input("Nama kontak yang ingin diupdate emailnya: ")
            if nama in kontak:
                email_baru = input("Email baru: ")
                kontak[nama][1] = email_baru
                print("Email berhasil diperbarui.")
            else:
                print("Kontak tidak ditemukan.")

        elif pilihan == "5":
            nama = input("Nama kontak yang ingin dihapus: ")
            if nama in kontak:
                del kontak[nama]
                print("Kontak berhasil dihapus.")
            else:
                print("Kontak tidak ditemukan.")

        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid.")
            
main()