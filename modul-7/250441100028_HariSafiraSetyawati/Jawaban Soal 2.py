# Program Manajemen Inventaris Gudang (CRUD)

inventaris = {}  

def tampilkan_semua():
    if not inventaris:
        print("\nBelum ada data barang.\n")
    else:
        print("\n=== DAFTAR SEMUA BARANG ===")
        for id_barang, data in inventaris.items():
            print(f"ID        : {id_barang}")
            print(f"Nama      : {data[0]}")
            print(f"Harga     : {data[1]}")
            print(f"Stok      : {data[2]}")
            print("-" * 35)
        print()

def cari_barang():
    id_barang = input("Masukkan ID barang yang dicari: ")
    
    if id_barang in inventaris:
        print("\nBarang ditemukan:")
        print(f"ID        : {id_barang}")
        print(f"Nama      : {inventaris[id_barang][0]}")
        print(f"Harga     : {inventaris[id_barang][1]}")
        print(f"Stok      : {inventaris[id_barang][2]}\n")
    else:
        print("\nBarang dengan ID tersebut tidak ditemukan!\n")

def tambah_barang():
    id_barang = input("Masukkan ID barang: ")

    if id_barang in inventaris:
        print("ID tersebut sudah ada! Gunakan ID lain.\n")
        return

    nama = input("Masukkan nama barang: ")
    try:
        harga = float(input("Masukkan harga barang: "))
        stok = int(input("Masukkan jumlah stok: "))
    except ValueError:
        print("Input harga/stok harus berupa angka!\n")
        return

    if stok < 0:
        print("Stok tidak boleh negatif!\n")
        return

    inventaris[id_barang] = [nama, harga, stok]
    print("Barang berhasil ditambahkan!\n")

def update_stok():
    id_barang = input("Masukkan ID barang yang ingin diperbarui stoknya: ")

    if id_barang not in inventaris:
        print("Barang tidak ditemukan!\n")
        return

    try:
        perubahan = int(input("Masukkan perubahan stok (+ untuk menambah, - untuk mengurangi): "))
    except ValueError:
        print("Perubahan stok harus berupa angka!\n")
        return

    stok_sekarang = inventaris[id_barang][2]
    stok_baru = stok_sekarang + perubahan

    if stok_baru < 0:
        print("Stok tidak boleh negatif! Pembaruan dibatalkan.\n")
        return

    inventaris[id_barang][2] = stok_baru
    print("Stok berhasil diperbarui!\n")


def hapus_barang():
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")

    if id_barang in inventaris:
        del inventaris[id_barang]
        print("Barang berhasil dihapus!\n")
    else:
        print("Barang tidak ditemukan!\n")

# ===== MENU UTAMA =====
while True:
    print("=== MENU INVENTARIS GUDANG ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang berdasarkan ID")
    print("3. Tambah barang baru")
    print("4. Perbarui stok barang")
    print("5. Hapus barang")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_semua()
    elif pilihan == "2":
        cari_barang()
    elif pilihan == "3":
        tambah_barang()
    elif pilihan == "4":
        update_stok()
    elif pilihan == "5":
        hapus_barang()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.\n")