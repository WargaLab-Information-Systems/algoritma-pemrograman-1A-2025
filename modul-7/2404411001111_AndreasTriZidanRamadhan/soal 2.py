inventaris = []
id = 1
def tambah_barang(id):
    nama = input("Masukkan nama barang: ")
    for item in inventaris:
        if item["nama"] == nama:
            print("Barang sudah ada! Gunakan nama lain atau update barang.")
            return

    jumlah = int(input("Masukkan jumlah barang: "))
    if jumlah < 0:
        print("Jumlah barang tidak boleh negatif.")
        return
    harga = int(input("Masukkan harga barang: "))
    if harga < 0:
        print("Harga barang tidak boleh negatif.")
        return
    barang = {
        "id": id,
        "nama": nama,
        "jumlah": jumlah,
        "harga": harga
    }

    inventaris.append(barang)
    print("Barang berhasil ditambahkan!")
    return id + 1


def tampilkan_barang():
    if inventaris:
        for item in inventaris:
            print(f"\n  ID    : {item['id']}")
            print(f"  Nama  : {item['nama']}")
            print(f"  Jumlah: {item['jumlah']}")
            print(f"  Harga : {item['harga']}")
    else:
        print("Inventaris kosong.")


def update_barang():
    nama = input("Masukkan nama barang yang ingin diupdate: ")

    for item in inventaris:
        if item["nama"] == nama:
            item["jumlah"] = int(input("Masukkan jumlah baru: "))
            item["harga"] = int(input("Masukkan harga baru: "))
            print("Barang berhasil diupdate!")
            return
    
    print("Barang tidak ditemukan.")


def hapus_barang():
    nama = input("Masukkan nama barang yang ingin dihapus: ")

    for item in inventaris:
        if item["nama"] == nama:
            inventaris.remove(item)
            print("Barang berhasil dihapus!")
            return

    print("Barang tidak ditemukan.")


def cari_barang():
    id_input = int(input("Masukkan id barang yang ingin dicari: "))
    for item in inventaris:
        if item["id"] == id_input:
            print("\nBarang ditemukan:")
            print(f"ID    : {item['id']}")
            print(f"Nama  : {item['nama']}")
            print(f"Jumlah: {item['jumlah']}")
            print(f"Harga : {item['harga']}")
            return

    print("Barang tidak ditemukan.")


while True:
    print("\n===== Inventaris Barang =====")
    print("1. Tambah Barang")
    print("2. Tampilkan Barang")
    print("3. Update Barang")
    print("4. Hapus Barang")
    print("5. Cari Barang")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == '1':
        id = tambah_barang(id)
    elif pilihan == '2':
        tampilkan_barang()
    elif pilihan == '3':
        update_barang()
    elif pilihan == '4':
        hapus_barang()
    elif pilihan == '5':
        cari_barang()
    elif pilihan == '6':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid.")
