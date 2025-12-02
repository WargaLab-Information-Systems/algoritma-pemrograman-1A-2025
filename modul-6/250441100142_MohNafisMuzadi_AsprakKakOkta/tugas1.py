data_kunjungan = []
id_antrian = 1

while True:
    print("\n 1. Tambah Data Pengunjung\n 2. Tampilkan semua data\n 3. Hapus Data\n 4. Keluar")

    menu = input("Pilih menu (1-4): ")

    if menu == "1":
        print("\nTambah Data Pengunjung")
        nama_pengunjung = input("Nama pengunjung: ")
        nama_santri = input("Nama santri yang dijenguk: ")
        daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").lower()

        if daerah == "sumatra" or daerah == "kalimantan" or daerah == "jawa":
            data_kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah])
            print("Data berhasil ditambahkan dengan ID:", id_antrian)
            id_antrian += 1
        else:
            print("Daerah tidak valid! Harus Sumatra, Kalimantan, atau Jawa.")

    elif menu == "2":
        print("\nDaftar Pengunjung Berdasarkan Daerah")

        if len(data_kunjungan) == 0:
            print("Belum ada data kunjungan.")
        else:
            print("\nPengunjung dari Sumatra:")
            ada = False
            for data in data_kunjungan:
                if data[3] == "sumatra":
                    print("ID:", data[0], "| Nama:", data[1], "| Santri:", data[2], "| Daerah:", data[3])
                    ada = True
            if not ada:
                print("Tidak ada data dari Sumatra.")

            print("\nPengunjung dari Kalimantan:")
            ada = False
            for data in data_kunjungan:
                if data[3] == "kalimantan":
                    print("ID:", data[0], "| Nama:", data[1], "| Santri:", data[2], "| Daerah:", data[3])
                    ada = True
            if not ada:
                print("Tidak ada data dari Kalimantan.")

            print("\nPengunjung dari Jawa:")
            ada = False
            for data in data_kunjungan:
                if data[3] == "jawa":
                    print("ID:", data[0], "| Nama:", data[1], "| Santri:", data[2], "| Daerah:", data[3])
                    ada = True
            if not ada:
                print("Tidak ada data dari Jawa.")

    elif menu == "3":
        print("\nHapus Data")
        if len(data_kunjungan) == 0:
            print("Belum ada data yang bisa dihapus.")
        else:
            hapus = int(input("Masukkan ID yang ingin dihapus: "))
            ketemu = False
            for data in data_kunjungan:
                if data[0] == hapus:
                    data_kunjungan.remove(data)
                    print("Data dengan ID", hapus, "berhasil dihapus.")
                    ketemu = True
                    break
            if ketemu == False:
                print("ID tidak ditemukan!")

    elif menu == "4":
        print("GoodBye")
        break

    else:
        print("Pilihan tidak valid!")
