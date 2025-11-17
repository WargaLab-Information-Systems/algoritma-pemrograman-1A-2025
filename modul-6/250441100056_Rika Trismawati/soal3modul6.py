angka = []  # list data

while True:
    print("\n=== MENU CRUD ===")
    print("1. Tambah Angka")
    print("2. Tampilkan Data")
    print("3. Ubah Angka (berdasarkan nilai)")
    print("4. Hapus Angka (berdasarkan nilai)")
    print("5. Cek Pembagian Dua Bagian Sama")
    print("6. Keluar")

    pilih = int(input("Pilih menu: "))

    if pilih == 1:  # Create
        data = int(input("Masukkan angka: "))
        angka.append(data)
        print("Data berhasil ditambah!")

    elif pilih == 2:  # Read
        print("Data saat ini:", angka)

    elif pilih == 3:  # Update tanpa index
        print("Data angka:", angka)
        lama = int(input("Masukkan angka yang ingin diubah: "))

        if lama in angka:
            baru = int(input("Masukkan nilai baru: "))
            angka.remove(lama)
            angka.append(baru)
            print("Data berhasil diubah!")
        else:
            print("Angka tidak ditemukan!")

    elif pilih == 4:  # Delete tanpa index
        print("Data angka:", angka)
        hapus = int(input("Masukkan angka yang ingin dihapus: "))

        if hapus in angka:
            angka.remove(hapus)
            print("Data berhasil dihapus!")
        else:
            print("Angka tidak ditemukan!")

    elif pilih == 5:  # Cek pembagian sama
        total = 0
        for x in angka:
            total += x
        
        jumlah_kiri = 0
        bisa = False

        for i in range(len(angka)-1):
            jumlah_kiri += angka[i]
            jumlah_kanan = total - jumlah_kiri

            if jumlah_kiri == jumlah_kanan:
                bisa = True
                break

        if bisa:
            print("True  Bisa dibagi menjadi dua bagian dengan jumlah sama")
        else:
            print("False Tidak bisa dibagi menjadi dua bagian sama")

    elif pilih == 6:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")