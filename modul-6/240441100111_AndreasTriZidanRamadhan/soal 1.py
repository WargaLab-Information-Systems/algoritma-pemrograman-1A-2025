data_kunjungan = []
id = 1

def tambah_kunjungan(id):
    nama_pengunjung = input("Nama pengunjung: ")
    nama_santri = input("Nama santri yang dijenguk: ")
    daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").lower()
    
    if daerah not in ["sumatra", "kalimantan", "jawa"]:
        print("Daerah tidak valid. Silakan masukkan Sumatra, Kalimantan, atau Jawa.")
        return

    data_kunjungan.append([id, nama_pengunjung, nama_santri, daerah])
    print(f"Data berhasil ditambahkan dengan ID Antrian {id}")
    return id + 1

def tampilkan_kunjungan():
    if not data_kunjungan:
        print("Belum ada data kunjungan.")
        return

    urutan = ["sumatra", "kalimantan", "jawa"]
    for daerah in urutan:
        print(f"\n=== Daerah {daerah} ===")
        for data in data_kunjungan:
            if data[3] == daerah:
                print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]}")

def hapus_kunjungan():
    id_hapus = int(input("Masukkan ID antrian yang ingin dihapus: "))
    for data in data_kunjungan:
        if data[0] == id_hapus:
            data_kunjungan.remove(data)
            print("Data berhasil dihapus.")
            return
    print("ID tidak ditemukan.")

while True:
    print("\n=== SISTEM KUNJUNGAN PONDOK AL-QOHOL ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        id = tambah_kunjungan(id)
    elif pilihan == "2":
        tampilkan_kunjungan()
    elif pilihan == "3":
        hapus_kunjungan()
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid.")
