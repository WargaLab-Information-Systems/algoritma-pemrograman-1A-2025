inventaris = {}

def input_angka(pesan):
    while True:
        nilai = input(pesan)
        if nilai.isdigit():
            return int(nilai) 
        print("ERROR: Input harus berupa angka!")

def menu_input():
    while True:
        pilih = input("Pilih menu (1-6): ")
        if pilih.isdigit() and 1 <= int(pilih) <= 6:
            return int(pilih)
        print("ERROR: Pilihan harus angka 1-6!")

def tampilkan_barang():
    if not inventaris:
        print("Belum ada barang.")
    else:
        print("\n=== DAFTAR BARANG ===")
        for ID, info in inventaris.items():
            print(f"ID    : {ID}")
            print(f"Nama  : {info[0]}")
            print(f"Harga : {info[1]}")
            print(f"Stok  : {info[2]}")
            print("----------------------")

def cari_barang ():
    ID = input("masukkan id barang yang ingin dicari:")
    if ID in inventaris: 
        print(f"Nama    : {inventaris[ID][0]}")
        print(f"Harga   : {inventaris[ID][1]}")
        print(f"Stok    : {inventaris[ID][2]}")
    else :
        print("tidak ada barangnya")
        
def tambah_barang():
    ID = input("Masukkan ID barang baru: ")
    if ID in inventaris:
        print("ERROR: ID sudah ada.")
        return

    nama = input("Masukkan nama barang: ")
    harga = input_angka("Masukkan harga barang (angka): ")
    stok = input_angka("Masukkan stok barang (angka): ")

    inventaris[ID] = [nama, harga, stok]
    print("Barang berhasil ditambahkan.")

def update_stok():
    ID = input("Masukkan ID barang yang ingin diupdate: ")
    if ID not in inventaris:
        print("Barang tidak ditemukan.")
        return

    perubahan = input_angka("Masukkan perubahan stok : ")

    stok_baru = inventaris[ID][2] = perubahan
    if stok_baru < 0:
        print("ERROR: Stok tidak boleh negatif!")
    else:
        inventaris[ID][2] = stok_baru
        print("Stok berhasil diperbarui.")

def hapus_barang():
    ID = input("Masukkan ID barang yang ingin dihapus: ")
    if ID in inventaris:
        del inventaris[ID]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

while True:
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang berdasarkan ID")
    print("3. Tambah barang baru")
    print("4. Update stok barang")
    print("5. Hapus barang")
    print("6. Keluar")

    pilihan = menu_input()

    if pilihan == 1:
        tampilkan_barang()
    elif pilihan == 2:
        cari_barang()
    elif pilihan == 3:
        tambah_barang()
    elif pilihan == 4:
        update_stok()
    elif pilihan == 5:
        hapus_barang()
    elif pilihan == 6:
        print("Program selesai.")
        break
