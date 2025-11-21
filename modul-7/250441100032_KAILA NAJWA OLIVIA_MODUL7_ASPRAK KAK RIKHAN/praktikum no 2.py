# Program Manajemen Inventaris Gudang
inventaris = {}  

def tampilkan_barang():
    if inventaris:
        print("\n=== DAFTAR BARANG DI GUDANG ===")
        print("ID | Nama Barang | Harga | Stok")
        for id_barang, data in inventaris.items():
            print(f"{id_barang} | {data[0]} | Rp{data[1]} | {data[2]}")
    else:
        print("\nTidak ada barang dalam inventaris.")

def cari_barang():
    id_cari = input("Masukkan ID barang yang dicari: ").upper()
    if not id_cari.isalnum():
        print("ID hanya boleh berisi huruf dan angka!")
        return
    elif id_cari in inventaris:
        data = inventaris[id_cari]
        print("\n=== BARANG DITEMUKAN ===")
        print(f"ID    : {id_cari}")
        print(f"Nama  : {data[0]}")
        print(f"Harga : Rp{data[1]}")
        print(f"Stok  : {data[2]}")
    else:
        print("\nBarang dengan ID tersebut tidak ditemukan!")

def tambah_barang():
    id_barang = input("Masukkan ID barang harus berupa angka dan huruf: ")
    if not id_barang.isalnum():
        print("ID hanya boleh berisi huruf dan angka!")
        return 
    elif id_barang in inventaris:
        print("ID sudah ada! Gunakan ID lain.")
    else:
        nama = input("Masukkan nama barang: ")
        harga = float(input("Masukkan harga barang: "))
        stok = int(input("Masukkan stok barang: "))
        inventaris[id_barang] = [nama, harga, stok]
        print("Barang berhasil ditambahkan!")

def update_stok():
    id_barang = input("Masukkan ID barang yang akan diperbarui stoknya: ")
    if id_barang in inventaris:
        stok_baru = int(input("Masukkan jumlah stok baru (stok tidak boleh negatif): "))
        if stok_baru < 0:
            print("Stok tidak boleh negatif!")
        else:
            inventaris[id_barang][2] = stok_baru
            print("Stok berhasil diperbarui!")
    else:
        print("Barang tidak ditemukan!")

def hapus_barang():
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")
    if id_barang in inventaris:
        del inventaris[id_barang]
        print("Barang berhasil dihapus!")
    else:
        print("Barang tidak ditemukan!")

# MENU UTAMA
while True:
    print("\n=== MENU INVENTARIS GUDANG ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang berdasarkan ID")
    print("3. Tambah barang")
    print("4. Update stok barang")
    print("5. Hapus barang")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

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
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi!")