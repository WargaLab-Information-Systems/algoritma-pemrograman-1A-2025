data = []
id_antrian = 1

def tambah():
    global id_antrian
    nama_pengunjung = input("Masukkan nama pengunjung: ")
    nama_santri = input("Masukkan nama santri yang dijenguk: ")
    while True:
        daerah_asal = input("Masukkan daerah asal (sumatra/kalimantan/jawa): ").lower()
        if daerah_asal in ["sumatra", "kalimantan", "jawa"]:
            break
        else:
            print("Daerah tidak valid! masukkan daerah sesuai yang ditentukan!")
    data.append([id_antrian, nama_pengunjung, nama_santri, daerah_asal])
    print("Data berhasil ditambahkan dengan ID:", id_antrian)
    id_antrian += 1


def tampilkan():
    if not data:
        print("Belum ada data pengunjung.")
        return
    print("===== DAFTAR PENGUNJUNG SANTRI =====")
    urut = ["sumatra", "kalimantan", "jawa"]
    for d in urut:
        for x in data:
            if x[3].lower() == d:
                print(f"ID:{x[0]}  |  {x[1]} sedang menjenguk {x[2]} dari {x[3]}")

def hapus_data():
    if not data:
        print("Belum ada data yang dihapus.")
        return
    id_hapus = int(input("Masukkan ID pengunjung yang mau dihapus: "))
    for x in data:
        if x[0] == id_hapus:
            data.remove(x)
            print("Data berhasil dihapus.")
            return
    print("ID Failed.")

#Program utamanya
while True:
    print("====== Menu data kujungan santri ======")
    print("1. Tambah Pengunjung")
    print("2. Tampilkan daftar pengunjung")
    print("3. Hapus pengunjung")
    print("4. Keluar")

    pilih_menu = input("Pilih menu (1-4): ")

    if pilih_menu == "1":
        tambah()
    elif pilih_menu == "2":
        tampilkan()
    elif pilih_menu == "3":
        hapus_data()
    elif pilih_menu == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")    

