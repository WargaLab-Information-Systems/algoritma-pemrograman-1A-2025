def inventaris_gudang():
    inventaris = {}

    def tambah_barang(id_barang, nama_barang, harga, stok):
        if id_barang in inventaris:
            print("ID barang sudah ada.")
            return
        inventaris[id_barang] = [nama_barang, harga, stok]
        print("Barang berhasil ditambahkan.")

    def lihat_barang(id_barang):
        if id_barang in inventaris:
            print(f"ID: {id_barang}, Nama: {inventaris[id_barang][0]}, Harga: {inventaris[id_barang][1]}, Stok: {inventaris[id_barang][2]}")
        else:
            print("Barang tidak ditemukan.")

    def ubah_stok(id_barang, stok_baru):
        if id_barang in inventaris:
            if stok_baru < 0:
                print("Stok tidak boleh negatif.")
                return
            inventaris[id_barang][2] = stok_baru
            print("Stok berhasil diubah.")
        else:
            print("Barang tidak ditemukan.")

    def hapus_barang(id_barang):
        if id_barang in inventaris:
            del inventaris[id_barang]
            print("Barang berhasil dihapus.")
        else:
            print("Barang tidak ditemukan.")
            
    def tampilkan_semua_barang():
        if not inventaris:
            print("Tidak ada barang yang tersimpan.")
        else:
            print("\nDaftar Barang:")
            for id_barang, detail in inventaris.items():
                print(f"ID: {id_barang}, Nama: {detail[0]}, Harga: {detail[1]}, Stok: {detail[2]}")

    while True:
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Lihat Barang")
        print("3. Ubah Stok")
        print("4. Hapus Barang")
        print("5. Tampilkan Semua Barang")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            id_barang = input("Masukkan ID barang: ")
            nama_barang = input("Masukkan nama barang: ")
            harga = float(input("Masukkan harga: "))
            stok = int(input("Masukkan stok: "))
            tambah_barang(id_barang, nama_barang, harga, stok)

        elif pilihan == '2':
            id_barang = input("Masukkan ID barang yang ingin dilihat: ")
            lihat_barang(id_barang)

        elif pilihan == '3':
            id_barang = input("Masukkan ID barang yang ingin diubah stoknya: ")
            if id_barang not in inventaris:
                print("Barang tidak ditemukan.")
                continue
            stok_baru = int(input("Masukkan stok baru: "))
            ubah_stok(id_barang, stok_baru)

        elif pilihan == '4':
            id_barang = input("Masukkan ID barang yang ingin dihapus: ")
            if id_barang not in inventaris:
                print("Barang tidak ditemukan.")
                continue
            hapus_barang(id_barang)

        elif pilihan == '5':
            tampilkan_semua_barang()

        elif pilihan == '6':
            print("Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid.")

# Inisialisasi program
inventaris_gudang()