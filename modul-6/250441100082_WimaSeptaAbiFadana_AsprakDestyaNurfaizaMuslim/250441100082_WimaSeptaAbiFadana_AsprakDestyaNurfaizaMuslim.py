data = []

def tambah_data():

    pengunjung = input("masukkan nama pengunjung : ")
    santri = input("masukan nama santri yang di jenguk : ")

    print("pilih daerah asal anda : ")
    print("1. sumatra")
    print("2. kalimantan")
    print("3. jawa")
    pilih = input("masukan pilihan (1, 2, 3) : ")
    
    if pilih == "1":
        daerah = "sumatra"
    elif pilih == "2":
        daerah = "kalimantan"
    elif pilih == "3":
        daerah = "jawa"
    else:
        print("pilihan tidak tersedia!")
        return

    id_antrean = 1
    for i in data:
        id_antrean += 1

    data_baru = [pengunjung, santri, daerah, id_antrean]

    data.append(data_baru)

    print("data berhasil ditambah dengan id antrean ", id_antrean)

def tampilan_data():
    if data == []:
        print("belum ada data pengunjung")
        return

    urut_daerah = ["sumatra", "kalimantan", "jawa"]

    print("----- daftar kunjungan -----")

    for daerah in urut_daerah:
        ada_data = False
        print("--- Pengunjung dari", daerah, "---")

        for d in data:
            if d[2] == daerah:
                print("ID", d[3], "| pengunjung :", d[0], "| santri :", d[1])
                ada_data = True

        if not ada_data:
            print("Tidak ada pengunjung dari daerah ini.")

def hapus_data():
    if data == []:
        print("belum ada data untuk dihapus")
        return

    id_input = input("masukkan ID yang ingin dihapus : ")

    angka = "0123456789"
    for c in id_input:
        if c not in angka:
            print("ID harus berupa angka!")
            return

    id_hps = int(id_input)

    ditemukan = False

    for d in data:
        if d[3] == id_hps:
            data.remove(d)
            print("data dengan ID", id_hps, "berhasil dihapus")
            ditemukan = True
            break

    if not ditemukan:
        print("ID tidak ditemukan")

while True:
    print("----- pilih menu kunjungan santri -----")
    print("1. tambah data pengunjung")
    print("2. tampilkan semua pengunjung")
    print("3. hapus data pengunjung")
    print("4. keluar")

    menu = input("pilih menu (1,2,3,4) : ")

    if menu == "1":
        tambah_data()
    elif menu == "2":
        tampilan_data()
    elif menu == "3":
        hapus_data()
    elif menu == "4":
        print("terimakasih")
        break
    else:
        print("pilihan tidak valid")
