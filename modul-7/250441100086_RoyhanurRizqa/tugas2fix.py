inventaris = {}

def tambah_barang():
    ID = input("ID barang: ")
    if ID in inventaris:
        print("ID sudah ada di daftar,silahkan pilih update apabila ingin menambah stok\n")
        return
    nama = input("Nama barang: ")
    harga = int(input("Harga: "))
    stok = int(input("Stok: "))
    inventaris[ID] = [nama, harga, stok]
    print("Barang berhasil ditambahkan!\n")

def update_stok():
    ID = input("Masukkan ID barang: ")
    if ID in inventaris:
        while True:
            perubahan = (input("pilih antara (Tambah/Kurang) stok: ").lower())
            if perubahan == "tambah":
                tambah=int(input("masukkan angka yang ingin ditambahkan: "))
                stok_baru = inventaris[ID][2] + tambah
                break
            elif perubahan == "kurang":
                kurang=int(input("masukkan angka yang ingin dikurangi: "))
                stok_baru = inventaris[ID][2] - kurang
                if stok_baru < 0:
                    print("Stok tidak boleh negatif!\n")
                    continue
                else:
                    break
            else:
                print("masukkan 'tambah' atau 'kurang'")
                continue
    
        inventaris[ID][2] = stok_baru
        print("Stok berhasil diperbarui!\n")

    else:
        print("Barang tidak ditemukan.\n")

def cari_barang():
    ID = input("Masukkan ID barang: ")
    if ID in inventaris:
        print(f"Nama  : {inventaris[ID][0]}")
        print(f"Harga : {inventaris[ID][1]}")
        print(f"Stok  : {inventaris[ID][2]}\n")
    else:
        print("Barang tidak ditemukan.\n")

def tampil_semua():
    if not inventaris:
        print("Belum ada data barang.\n")
        return
    for ID, data in inventaris.items():
        print(f"ID    : {ID}")
        print(f"Nama  : {data[0]}")
        print(f"Harga : {data[1]}")
        print(f"Stok  : {data[2]}\n")

def hapus_barang():
    ID = input("Masukkan ID barang: ")
    if ID in inventaris:
        del inventaris[ID]
        print("Barang berhasil dihapus.\n")
    else:
        print("Barang tidak ditemukan.\n")

while True:
    print("=== INVENTARIS GUDANG ===")
    print("1.tambah barang")
    print("2.update stok")
    print("3.cari barang")
    print("4.tampilkan semua barang")
    print("5.Hapus barang")
    print("6.Keluar")

    pilih = input("Pilih menu: ")
    if pilih == "1":
        tambah_barang()
    elif pilih == "2":
        update_stok()
    elif pilih == "3":
        cari_barang()
    elif pilih == "4":
        tampil_semua()
    elif pilih == "5":
        hapus_barang()
    elif pilih == "6":
        print("Program selesai.terima kasih")
        break
    else:
        print("Pilihan tidak valid.\n")