data_kunjungan = []
nomer_antrian = 1  
while True:
    print("\n=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Keluar")
    menu = input("Pilih menu (1-4): ")
    if menu == "1":
        nama_pengunjung = input("Nama pengunjung: ")
        nama_santri = input("Nama santri yang dijenguk: ")
        daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()

        if daerah == "Sumatra" or daerah == "Kalimantan" or daerah == "Jawa":
            data_kunjungan.append([nomer_antrian, nama_pengunjung, nama_santri, daerah])
            print("Data berhasil ditambahkan! ID antrian:", nomer_antrian)
            nomer_antrian += 1
        else:
            print("Daerah tidak valid! Harus Sumatra, Kalimantan, atau Jawa.")

    elif menu == "2":
        if len(data_kunjungan) == 0:
            print("tidak ada data kunjungan.")
        else:
            for daerah in ["Sumatra", "Kalimantan", "Jawa"]:
                print("\n--- Pengunjung dari", daerah, "---")
                ada = False
                for data in data_kunjungan:
                    if data[3] == daerah:
                        print("ID:", data[0], "| Pengunjung:", data[1], "| Santri:", data[2])
                        ada = True
                if not ada:
                    print("(Tidak ada pengunjung dari daerah ini.)")

    elif menu == "3":
        if len(data_kunjungan) == 0:
            print("Belum ada data untuk dihapus.")
        else:
            id_hapus = input("Masukkan ID yang ingin dihapus: ")

            if id_hapus.isdigit():
                id_hapus = int(id_hapus)
                ditemukan = False
                for data in data_kunjungan:
                    if data[0] == id_hapus:
                        data_kunjungan.remove(data)
                        print("Data dengan ID", id_hapus, "berhasil dihapus.")
                        ditemukan = True
                    
                if not ditemukan:
                    print("ID tidak ditemukan.")
            else:
                print("ID harus berupa angka!")

    elif menu == "4":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
