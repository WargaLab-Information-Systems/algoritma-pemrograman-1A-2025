data_kunjungan = []

def tambah_data():
    print("\n=== INPUT DATA KUNJUNGAN SANTRI ===")
    nama_pengunjung = input("Masukkan nama pengunjung     : ")
    nama_santri = input("Masukkan nama santri yang dijenguk : ")

    while True:
        daerah = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if daerah in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        else:
            print("Input daerah tidak valid! Harus: Sumatra / Kalimantan / Jawa")

    id_antrian = len(data_kunjungan) + 1

    data_kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah])
    print(f"Data berhasil ditambahkan dengan ID antrian: {id_antrian}\n")

def tampilkan_data():
    print("\n=== DAFTAR KUNJUNGAN SANTRI (Dikelompokkan Berdasarkan Daerah) ===")

    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]

    for daerah in urutan_daerah:
        print(f"\n-- Pengunjung dari {daerah} --")
        count = 0
        for data in data_kunjungan:
            if data[3] == daerah:
                print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]}")
                count += 1
        if count == 0:
            print("Tidak ada data.")

def hapus_data():
    print("\n=== HAPUS DATA PENGUNJUNG ===")
    try:
        target_id = int(input("Masukkan ID antrian yang ingin dihapus: "))
        for data in data_kunjungan:
            if data[0] == target_id:
                data_kunjungan.remove(data)
                print(f"Data dengan ID {target_id} berhasil dihapus!\n")

                for i in range(len(data_kunjungan)):
                    data_kunjungan[i][0] = i + 1
                return
        print("ID tidak ditemukan!\n")
    except ValueError:
        print("Input harus berupa angka!\n")

while True:
    print("==== SISTEM KUNJUNGAN SANTRI ====")
    print("1. Tambah Data Pengunjung")
    print("2. Tampilkan Daftar Pengunjung")
    print("3. Hapus Data Pengunjung")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih 1 - 4.\n")