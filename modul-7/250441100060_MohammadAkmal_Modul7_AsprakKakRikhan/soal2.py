data_barang = {}

def tampilkan_semua():
    if not data_barang:
        print("\nBelum ada data barang.\n")
        return

    print("\n=== Daftar Barang ===")
    for kode, data in data_barang.items():
        print(f"ID: {kode}")
        print(f"  Nama  : {data[0]}")
        print(f"  Harga : {data[1]}")
        print(f"  Stok  : {data[2]}")
        print("-" * 30)
    print()

def cari_barang():
    kode = input("Masukkan ID barang: ").strip()
    if kode in data_barang:
        nama, harga, stok = data_barang[kode]
        print("\n=== Data Barang ===")
        print(f"ID    : {kode}")
        print(f"Nama  : {nama}")
        print(f"Harga : {harga}")
        print(f"Stok  : {stok}\n")
    else:
        print("Barang dengan ID tersebut tidak ditemukan.\n")

def tambah_barang():
    kode = input("ID barang : ").strip()
    if kode in data_barang:
        print("ID sudah digunakan. Gunakan ID lain.\n")
        return

    nama = input("Nama barang   : ").strip()
    
    try:
        harga = int(input("Harga    : "))
        stok = int(input("Stok      : "))
    except ValueError:
        print("Harga dan stok harus berupa angka dan tidak boleh kosong.\n")
        return

    data_barang[kode] = [nama, harga, stok]
    if nama in data_barang:
        print("nama tidak boleh mengandung angka dan symbol")
        return
    print("Barang berhasil ditambahkan.\n")

def update_stok():
    kode = input("Masukkan ID barang: ").strip()
    if kode not in data_barang:
        print("Barang tidak ditemukan.\n")
        return

    try:
        perubahan = int(input("Perubahan stok (boleh negatif): "))
    except ValueError:
        print("Input tidak valid.\n")
        return

    stok_lama = data_barang[kode][2]
    stok_baru = stok_lama + perubahan

    if stok_baru < 0:
        print("Stok tidak boleh negatif.\n")
        return

    data_barang[kode][2] = stok_baru
    print("Stok berhasil diperbarui.\n")

def hapus_barang():
    kode = input("Masukkan ID barang: ").strip()
    if kode in data_barang:
        data_barang.pop(kode)
        print("Barang berhasil dihapus.\n")
    else:
        print("Barang tidak ditemukan.\n")

def menu():
    while True:
        print("=== DATA BARANG ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan ID")
        print("3. Tambah barang")
        print("4. Perbarui stok barang")
        print("5. Hapus barang")
        print("6. Keluar")

        opsi_pilihan = input("Pilih menu (1-6): ").strip()

        if opsi_pilihan == "1":
            tampilkan_semua()
        elif opsi_pilihan == "2":
            cari_barang()
        elif opsi_pilihan == "3":
            tambah_barang()
        elif opsi_pilihan == "4":
            update_stok()
        elif opsi_pilihan == "5":
            hapus_barang()
        elif opsi_pilihan == "6":
            print("Program selesai. Semoga harimu menyenangkan teman🤩😊")
            break
        else:
            print("Pilihan tidak valid.\n")

menu()