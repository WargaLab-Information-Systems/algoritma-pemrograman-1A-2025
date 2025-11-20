inventaris = {}

def tampilkan_barang():
    if not inventaris:
        print("Tidak ada data barang.")
    else:
        print("-----DAFTAR BARANG-----")
        for id_brg, data in inventaris.items():
            print("ID:", id_brg, "Nama:", data[0], "Harga:", data[1], "Stok:", data[2])
    print()

def cari_barang():
    id_brg = input("Masukkan ID barang yang dicari: ")
    if id_brg in inventaris:
        data = inventaris[id_brg]
        print("Nama:", data[0], "Harga:", data[1], "Stok:", data[2])
    else:
        print("Barang tidak ditemukan.")
    print()

def tambah_barang():
    id_brg = input("Masukkan ID barang: ")

    angka = "0123456789"
    if id_brg not in angka:
        print("ID harus berupa angka!")
    else:
        nama = input("Masukkan nama barang: ")
        harga = int(input("Masukkan harga barang: "))
        stok = int(input("Masukkan stok barang: "))

        inventaris[id_brg] = [nama, harga, stok]
        print("Barang berhasil ditambahkan!")
    print()

def update_stok():
    id_brg = input("Masukkan ID barang yang ingin diperbarui stoknya: ")
    if id_brg not in inventaris:
        print("Barang tidak ditemukan!")
        return

    print("Stok saat ini:", inventaris[id_brg][2])
    perubahan = int(input("Masukkan perubahan stok (+ untuk menambah, - untuk mengurangi): "))

    stok_awal = inventaris[id_brg][2]
    stok_baru = stok_awal + perubahan

    if stok_baru < 0:
        print("Stok tidak boleh negatif!")
        return

    inventaris[id_brg][2] = stok_baru
    print("Stok berhasil diperbarui. Stok baru:", stok_baru)
    print()

def hapus_barang():
    id_brg = input("Masukkan ID barang yang ingin dihapus: ")
    if id_brg in inventaris:
        del inventaris[id_brg]
        print("Barang berhasil dihapus!")
    else:
        print("Barang tidak ditemukan")

while True:
    print("=== MENU INVENTARIS GUDANG ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang")
    print("3. Tambah barang baru")
    print("4. Perbarui stok barang")
    print("5. Hapus barang")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_barang()
    elif pilihan == "2":
        cari_barang()
    elif pilihan == "3":
        tambah_barang()
    elif pilihan == "4":
        update_stok()
    elif pilihan == "5":
        hapus_barang()
    else:
        print("Pilihan tidak valid!")
