def main():
    inventaris = {
        "1": ["Kursi", 150000, 5],
        "2": ["Meja", 300000, 2]
    }

    while True:
        print("==========================")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang")
        print("3. Tambah Barang Baru")
        print("4. Update Stok Barang")
        print("5. Hapus Barang") 
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            if not inventaris:
                print("Belum ada data barang.")
            else:
                for kode, data in inventaris.items():
                    print(f"{kode}: Nama barang = {data[0]}, Harga = {data[1]}, Stok = {data[2]}")

        elif pilihan == "2":
            kode = input("Masukkan ID barang: ")
            if kode in inventaris:
                print(f"Nama barang = {inventaris[kode][0]}, Harga = {inventaris[kode][1]}, Stok = {inventaris[kode][2]}")
            else:
                print("Barang tidak ditemukan.")

        elif pilihan == "3":
            while True:
                kode = input("ID barang: ")
                if kode in inventaris:
                    print("ID sudah ada! Silakan pilih ID lain.")
                else:
                    break

            nama = input("Nama barang: ")
            while True:
                harga = int(input("Harga: "))
                if harga < 0:
                    print("Harga tidak boleh minus")
                else:
                    break

            while True:
                stok = int(input("Stok: "))
                if stok < 0:
                    print("Stok tidak boleh minus")
                else:
                    break

            inventaris[kode] = [nama, harga, stok]
            print("Barang berhasil ditambahkan.")

        

        elif pilihan == "4":
            kode = input("ID barang yang ingin diupdate stoknya: ")
            if kode in inventaris:
                while True:
                    perubahan = int(input("Masukkan perubahan stok: "))
                    if perubahan < 0:
                        print("Stok tidak boleh negatif!")
                    else:
                        inventaris[kode][2] = perubahan
                        print("Stok berhasil diperbarui.")
                        break
            else:
                print("Barang tidak ditemukan.")

        elif pilihan == "5":
            kode = input("ID barang yang ingin dihapus: ")
            if kode in inventaris:
                del inventaris[kode]
                print("Barang berhasil dihapus.")
            else:
                print("Barang tidak ditemukan.")

        elif pilihan == "6":
            break

        else:
            print("Pilihan tidak valid.")

main()