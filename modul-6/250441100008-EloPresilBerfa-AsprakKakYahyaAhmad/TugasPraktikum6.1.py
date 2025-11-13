data = []
id_antrian = 1

def tambah(data, id_antrian):
    n_pengunjung = input("Nama pengunjung: ")
    while n_pengunjung == "":
        print("Nama pengunjung tidak boleh kosong!")
        n_pengunjung = input("Nama pengunjung: ")

    n_santri = input("Nama santri yang dijenguk: ")
    while n_santri == "":
        print("Nama santri tidak boleh kosong!")
        n_santri = input("Nama santri yang dijenguk: ")

    asal = input("Daerah asal (sumatra/kalimantan/jawa): ").lower()
    while asal not in ["sumatra", "kalimantan", "jawa"]:
        print("Daerah asal tidak valid.")
        asal = input("Masukkan daerah asal (sumatra/kalimantan/jawa): ").lower()

    data.append([id_antrian, n_pengunjung, n_santri, asal])
    print("Data berhasil ditambahkan (ID:", id_antrian, ")")
    return id_antrian + 1


def tampilkan(data):
    if not data:
        print("Belum ada data pengunjung.")
        return
    print("=== DAFTAR PENGUNJUNG SANTRI ===")
    urut = ["sumatra", "kalimantan", "jawa"]
    for asal in urut:
        for pengunjung in data:
            if pengunjung [3] == asal:
                print(f"ID:{pengunjung[0]} | Pengunjung : {pengunjung[1]} | Santri : {pengunjung[2]} | Asal: {pengunjung[3]}")


def hapus_data(data):
    if not data:
        print("Belum ada data untuk dihapus.")
        return
    id_hapus = input("Masukkan ID yang mau dihapus: ")
    while not id_hapus.isdigit():
        print("ID harus berupa angka.")
        id_hapus = input("Masukkan ID yang mau dihapus: ")
    for pengunjung in data:
        if pengunjung[0] == int(id_hapus):
            data.remove(pengunjung)
            print("Data berhasil dihapus.")
            return
    print("ID tidak ditemukan.")


while True:
    print("=== MENU KUNJUNGAN SANTRI ===")
    print("1. Tambah Pengunjung")
    print("2. Tampilkan Pengunjung")
    print("3. Hapus Pengunjung")
    print("4. Keluar")

    pilih = input("Pilih menu (1-4): ")
    if pilih == "1":
        id_antrian = tambah(data, id_antrian)
    elif pilih == "2":
        tampilkan(data)
    elif pilih == "3":
        hapus_data(data)
    elif pilih == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
