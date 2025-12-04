kunjungan = []
id_antrian = 1

def tambah_kunjungan():
    global id_antrian
    
    print("\n=== Tambah Data Kunjungan ===")
    nama_pengunjung = input("Nama Pengunjung        : ")
    nama_santri     = input("Nama Santri yang dijenguk : ")
    daerah          = input("Daerah (Sumatra/Kalimantan/Jawa): ")

    daerah = daerah.capitalize()

    if daerah not in ["Sumatra", "Kalimantan", "Jawa"]:
        print("Daerah tidak valid.\n")
        return

    data = [id_antrian, nama_pengunjung, nama_santri, daerah]
    kunjungan.append(data)

    print(f"\nData berhasil ditambahkan dengan id_antrian: {id_antrian}\n")
    id_antrian += 1


def tampilkan_kunjungan():
    print("\n=== Daftar Kunjungan Berdasarkan Daerah ===")

    if not kunjungan:
        print("Belum ada data kunjungan.\n")
        return

    urutan = ["Sumatra", "Kalimantan", "Jawa"]

    for asal in urutan:
        print(f"\n--- Pengunjung dari {asal} ---")
        ada = False
        for data in kunjungan:
            if data[3] == asal:
                print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]}\n")
                ada = True
        if not ada:
            print("Tidak ada pengunjung.")


def hapus_kunjungan():
    print("\n=== Hapus Data Kunjungan ===")
    try:
        hapus_id = int(input("Masukkan id_antrian yang ingin dihapus: "))
    except:
        print("ID harus berupa angka.\n")
        return

    for data in kunjungan:
        if data[0] == hapus_id:
            kunjungan.remove(data)
            print("Data berhasil dihapus.\n")
            return

    print("ID tidak ditemukan.\n")


while True:
    print("=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Kunjungan")
    print("2. Tampilkan Semua Kunjungan")
    print("3. Hapus Kunjungan")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_kunjungan()
    elif pilihan == "2":
        tampilkan_kunjungan()
    elif pilihan == "3":
        hapus_kunjungan()
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.\n")