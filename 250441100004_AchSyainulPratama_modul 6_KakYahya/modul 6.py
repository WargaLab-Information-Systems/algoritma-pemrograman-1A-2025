pengunjung = []
id_counter = 1

def tambah_pengunjung():
    global id_counter
    nama = input("Nama pengunjung: ")
    santri = input("Nama santri yang dijenguk: ")
    daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ")

    if daerah.lower() not in ["sumatra", "kalimantan", "jawa"]:
        print(" Daerah tidak valid! Hanya boleh Sumatra, Kalimantan, atau Jawa.\n")
        return  

    pengunjung.append([nama, santri, daerah, id_counter])
    id_counter += 1
    print(" Data berhasil ditambahkan!\n")

def tampilkan_pengunjung():
    print("\n=== Daftar Pengunjung ===")
    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
    for daerah in urutan_daerah:
        for p in pengunjung:
            if p[2].lower() == daerah.lower():
                print(f"ID {p[3]} | {p[0]} menjenguk {p[1]} dari {p[2]}")

def hapus_pengunjung():
    id_hapus = int(input("Masukkan ID antrian yang ingin dihapus: "))
    for p in pengunjung:
        if p[3] == id_hapus:
            pengunjung.remove(p)
            print(" Data berhasil dihapus!\n")
            return
    print(" ID tidak ditemukan!\n")

while True:
    print("1. Tambah pengunjung\n2. Tampilkan semua\n3. Hapus pengunjung\n4. Keluar")
    pilih = input("Pilih menu: ")
    if pilih == "1":
        tambah_pengunjung()
    elif pilih == "2":
        tampilkan_pengunjung()
    elif pilih == "3":
        hapus_pengunjung()
    elif pilih == "4":
        break
    else:
        print(" Pilihan tidak valid!\n")