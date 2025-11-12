kunjungan = []
id_hitung = 1

def tambah_kunjungan():
    while True:
        global id_hitung
        nama_pengunjung = input("Masukkan nama pengunjung: ")
        nama_santri = input("Masukkan nama santri yang dijenguk: ")
        daerah = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ").lower()
        if daerah not in ("sumatra","kalimantan","jawa"):
            print("masukkan antara sumatra/kalimantan/jawa")
            continue    
        kunjungan.append([id_hitung, nama_pengunjung, nama_santri, daerah])
        id_hitung += 1
        print("Data berhasil ditambahkan!\n")
        break

def tampilkan_kunjungan():
    urutan = ["sumatra", "kalimantan", "jawa"]
    for d in urutan:
        print(f"=== Pengunjung dari {d} ===")
        for data in kunjungan:
            if data[3] == d: 
                print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]} | Daerah: {data[3]}")
        print()

def hapus_kunjungan():
    id_hapus = int(input("Masukkan ID antrian yang ingin dihapus: "))
    for data in kunjungan:
        if data[0] == id_hapus:
            kunjungan.remove(data)
            print("Data berhasil dihapus!\n")
            return
    print("ID tidak ditemukan.\n")

while True:
    print("===== SISTEM KUNJUNGAN SANTRI =====")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Keluar")
    pilih = input("Pilih menu: ")
    
    if pilih == "1":
        tambah_kunjungan()
    elif pilih == "2":
        tampilkan_kunjungan()
    elif pilih == "3":
        hapus_kunjungan()
    elif pilih == "4":
        print("====== program selesai.terima kasih=====")
        break
    else:
        print("Pilihan tidak valid!\n")
        continue