print("="*10," TUGAS 1 MODUL 6 ","="*10)

data_kunjungan = []
id = 1 
while True:
    print("\n--- SISTEM KUNJUNGAN SANTRI ---")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Keluar")
    pilih = input("Pilih menu (1-4): ")
    if pilih == "1":
        pengunjung = input("Nama pengunjung: ")
        santri = input("Nama santri yang dijenguk: ")

        while True:
            daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
            if daerah in ["Sumatra", "Kalimantan", "Jawa"]:
                break
            else:
                print("Input salah! Pilih hanya antara Sumatra, Kalimantan, atau Jawa.")
        data_kunjungan.append([id, pengunjung, santri, daerah])
        print(f"Data berhasil ditambah dengan ID {id}")
        id += 1

    elif pilih == "2":
        if not data_kunjungan:
            print("Belum ada data kunjungan.")
        else:
            print("\n--- DATA KUNJUNGAN SANTRI ---")

            print("\nDaerah: Sumatra")
            for data in data_kunjungan:
                if data[3] == "Sumatra":
                    print(f"ID: {data[0]}, Pengunjung: {data[1]}, Santri: {data[2]}, Daerah: {data[3]}")

            print("\nDaerah: Kalimantan")
            for data in data_kunjungan:
                if data[3] == "Kalimantan":
                    print(f"ID: {data[0]}, Pengunjung: {data[1]}, Santri: {data[2]}, Daerah: {data[3]}")

            print("\nDaerah: Jawa")
        hapus_id = int(input("Masukkan ID yang ingin dihapus: "))
        ditemukan = False
        for data in data_kunjungan:
            if data[0] == hapus_id:
                data_kunjungan.remove(data)
                ditemukan = True
                print(f"Data dengan ID {hapus_id} berhasil dihapus.")
                break
        if not ditemukan:
            print("ID tidak ditemukan!")

    elif pilih == "4":
        print("Terima kasih, program selesai.")
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
