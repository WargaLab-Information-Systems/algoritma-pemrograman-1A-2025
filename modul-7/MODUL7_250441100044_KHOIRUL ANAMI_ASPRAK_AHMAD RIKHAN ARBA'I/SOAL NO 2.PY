X = "SOAL NO 2"
print(X)

inventory = {}  

def tampilkan_semua():
    if not inventory:
        print("Belum ada barang.")
    else:
        for item_id, data in inventory.items():
            print(f"ID: {item_id}, Nama: {data[0]}, Harga: {data[1]}, Stok: {data[2]}")

def cari_barang():
    item_id = input("Masukkan ID barang: ")
    if item_id in inventory:
        print(f"ID: {item_id}, Nama: {inventory[item_id][0]}, Harga: {inventory[item_id][1]}, Stok: {inventory[item_id][2]}")
    else:
        print("Barang tidak ditemukan.")

def tambahkan_barang():
    item_id = input("Masukkan ID baru: ")
    name = input("Nama barang: ")
    harga = int(input("Harga barang: "))
    stock = int(input("Stok barang: "))
    inventory[item_id] = [name, harga, stock]
    print("Barang berhasil ditambahkan.")

def perbarui_stok():
    item_id = input("Masukkan ID barang: ")
    if item_id in inventory:
        rubah = int(input("Masukkan perubahan stok (+ atau -): "))
        if inventory[item_id][2] + rubah < 0:
            print("Stok tidak boleh negatif!")
        else:
            inventory[item_id][2] += rubah
            print("Stok berhasil diperbarui.")
    else:
        print("Barang tidak ditemukan.")

def hapus_barang():
    item_id = input("Masukkan ID barang yang ingin dihapus: ")
    if item_id in inventory:
        del inventory[item_id]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

while True:
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang")
    print("3. Tambah barang")
    print("4. Update stok barang")
    print("5. Hapus barang")
    print("6. Keluar")

    pilihanmu = input("Pilih menu: ")

    if pilihanmu == "1":
        tampilkan_semua()
    elif pilihanmu == "2":
        cari_barang()
    elif pilihanmu == "3":
        tambahkan_barang()
    elif pilihanmu == "4":
        perbarui_stok()
    elif pilihanmu == "5":
        hapus_barang()
    elif pilihanmu == "6":
        break
    else:
        print("Input salah.")