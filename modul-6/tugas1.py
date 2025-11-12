
data_kunjungan = []   

def tambah_data():
    print("\n--- Tambah Data ---")

    nama = input("Nama Pengunjung: ")
    santri = input("Nama Santri yang dijenguk: ")
    asal = input("Asal (Sumatra/Kalimantan/Jawa): ")

    data_kunjungan.append([0, nama, santri, asal])

def urutkan_id():
    for i, data in enumerate(data_kunjungan, start=1):
        data[0] = i

def tampilkan_data():
    urutkan_id()
    print("\n--- Daftar Pengunjung Berdasarkan Daerah ---")

    sumatra = []
    kalimantan = []
    jawa = []

    for data in data_kunjungan:
        if data[3].lower() == "sumatra":
            sumatra.append(data)
        elif data[3].lower() == "kalimantan":
            kalimantan.append(data)
        elif data[3].lower() == "jawa":
            jawa.append(data)

    print("\n>> Pengunjung dari Sumatra:")
    for d in sumatra:
        print(d)

    print("\n>> Pengunjung dari Kalimantan:")
    for d in kalimantan:
        print(d)

    print("\n>> Pengunjung dari Jawa:")
    for d in jawa:
        print(d)


def hapus_data():
    urutkan_id()
    print("\n--- Hapus Data ---")
    
    hapus = int(input("Masukkan ID yang ingin dihapus: "))

    for data in data_kunjungan:
        if data[0] == hapus:
            data_kunjungan.remove(data)
            urutkan_id()
            print("Data berhasil dihapus!")
            return

    print("ID tidak ditemukan!")


while True:
    print("\n=== MENU ===")
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
        print("Pilihan tidak valid!")
