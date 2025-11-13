# Program Sistem Kunjungan Santri
# Menggunakan List yang berisi sublist [id_antrian, nama_pengunjung, nama_santri, daerah_asal]

data_kunjungan = []
id_counter = 1

def tambah_data():
    while True:
        global id_counter
        nama_pengunjung = input("Nama pengunjung: ")
        nama_santri = input("Nama santri yang dijenguk: ")
        daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if daerah not in ("Sumatra","Kalimantan","Jawa"):
            print ("inputan harus sumatra,kalimantan,jawa")
            continue
        data_kunjungan.append([id_counter, nama_pengunjung, nama_santri, daerah])
        print(f"Data berhasil ditambahkan dengan ID {id_counter}")
        id_counter += 1
        break
def tampilkan_data():
    if not data_kunjungan:
        print("Belum ada data kunjungan.")
        return

    print("\n=== DAFTAR PENGUNJUNG ===")
    for daerah in ["Sumatra", "Kalimantan", "Jawa"]:
        print(f"\n--- Pengunjung dari {daerah} ---")
        for data in data_kunjungan:
            if data[3] == daerah:
                print(f"ID {data[0]} | {data[1]} menjenguk {data[2]} ({data[3]})")

def hapus_data():
    id_hapus = int(input("Masukkan ID yang ingin dihapus: "))
    for data in data_kunjungan:
        if data[0] == id_hapus:
            data_kunjungan.remove(data)
            print("Data berhasil dihapus!")
            return
    print("ID tidak ditemukan.")

def menu():
    while True:
        print("\n--- MENU SISTEM KUNJUNGAN SANTRI ---")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            hapus_data()
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

menu()
