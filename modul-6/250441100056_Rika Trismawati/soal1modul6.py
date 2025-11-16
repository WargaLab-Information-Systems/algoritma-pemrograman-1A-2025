data = [] 
id_antrian = 1

while True:
    print("\n=== MENU SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Data Pengunjung")
    print("2. Tampilkan Semua Data (berdasarkan daerah)")
    print("3. Hapus Data Pengunjung (berdasarkan id)")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        print("\n--- Tambah Data Pengunjung ---")
        nama_pengunjung = input("Nama pengunjung: ")
        nama_santri = input("Nama santri yang dikunjungi: ")
        daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()

        # Tambahkan data ke list utama
        data.append([id_antrian, nama_pengunjung, nama_santri, daerah])
        print(f"Data berhasil ditambahkan dengan ID: {id_antrian}")
        id_antrian += 1

    elif pilihan == "2":
        print("\n--- Daftar Kunjungan Santri ---")

        # Menampilkan data urut berdasarkan daerah: Sumatra, Kalimantan, Jawa
        if len(data) == 0:
            print("Belum ada data pengunjung.")
        else:
            for daerah_urut in ["Sumatra", "Kalimantan", "Jawa"]:
                print(f"\nDaerah: {daerah_urut}")
                ada_data = False
                for d in data:
                    if d[3] == daerah_urut:
                        ada_data = True
                        print(f"ID: {d[0]}, Nama Pengunjung: {d[1]} , Santri: {d[2]}, Asal: {d[3]}")
                if not ada_data:
                    print("Masukkan data yang benar.")

    elif pilihan == "3":
        print("\n--- Hapus Data Pengunjung ---")
        hapus_id = int(input("Masukkan ID pengunjung yang ingin dihapus: "))
        ketemu = False

        for d in data:
            if d[0] == hapus_id:
                data.remove(d)
                ketemu = True
                print(f"Data dengan ID {hapus_id} berhasil dihapus.")
                break

        if not ketemu:
            print("ID tidak ditemukan!")

    elif pilihan == "4":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")