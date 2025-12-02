# Program Sistem Kunjungan Santri
# List utama untuk menyimpan data kunjungan

def tambah_data(daftar, nomor_id):
    print("\nTambah Data Kunjungan")
    nama_pengunjung = input("Nama Pengunjung : ")
    nama_santri = input("Nama Santri yang Dijenguk : ")
    while True:
        asal = input("Daerah Asal (Sumatra/Kalimantan/Jawa) : ").capitalize()
        if asal in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        print("Masukkan daerah asal yang benar!")
    daftar.append([nomor_id, nama_pengunjung, nama_santri, asal])
    print(f"Data berhasil ditambahkan dengan ID {nomor_id}")
    return nomor_id + 1


def tampil_data(daftar):
    if len(daftar) == 0:
        print("\nBelum ada data kunjungan.")
        return
    print("\nDaftar Kunjungan Santri Berdasarkan Daerah:")
    for daerah in ["Sumatra", "Kalimantan", "Jawa"]:
        print(f"\n-- Pengunjung dari {daerah} --")
        ada = False
        for data in daftar:
            if data[3] == daerah:
                print(f"ID:{data[0]} | Pengunjung:{data[1]} | Santri:{data[2]}")
                ada = True
        if not ada:
            print("Tidak ada pengunjung dari daerah ini.")

def hapus_data(daftar):
    if len(daftar) == 0:
        print("\nBelum ada data untuk dihapus.")
        return

    hapus_id_input = input("Masukkan ID yang akan dihapus : ")

    angka_valid = True
    for huruf in hapus_id_input:
        if huruf < "0" or huruf > "9":
            angka_valid = False
            break

    if not angka_valid:
        print("ID harus berupa angka.")
        return

    hapus_id = int(hapus_id_input)
    ditemukan = False
    for data in daftar:
        if data[0] == hapus_id:
            daftar.remove(data)
            print("Data berhasil dihapus.")
            ditemukan = True
            break
    if not ditemukan:
        print("ID tidak ditemukan.")

def utama():
    daftar_kunjungan = []
    nomor_id = 1

    while True:
        print("\n=== MENU SISTEM KUNJUNGAN SANTRI ===")
        print("1. Tambah Data Kunjungan")
        print("2. Tampilkan Semua Data")
        print("3. Hapus Data Kunjungan")
        print("4. Keluar dari Program")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            nomor_id = tambah_data(daftar_kunjungan, nomor_id)
        elif pilihan == "2":
            tampil_data(daftar_kunjungan)
        elif pilihan == "3":
            hapus_data(daftar_kunjungan)
        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak tersedia, silakan ulangi.")

utama()