# Program Struk Pembelian IndoMei

while True:
    nama = input("\nMasukkan nama pembeli: ")

    total = 0
    daftar_barang = []

    while True:
        barang = input("Masukkan nama barang: ")
        harga = int(input("Masukkan harga barang: "))

        daftar_barang.append((barang, harga))
        total += harga

        lagi = input("Tambah barang lagi? (y/n): ").lower()
        if lagi == 'n':
            break

    # Menampilkan struk
    print("\n===== STRUK PEMBELIAN =====")
    print("Nama Pembeli:", nama)
    print("-----------------------------")
    for barang, harga in daftar_barang:
        print(f"{barang} - Rp{harga}")
    print("-----------------------------")
    print("Total Harga: Rp", total)
    print("Terima kasih telah berbelanja di IndoMei.")
    print("=============================\n")

    pembeli_lagi = input("Apakah ada pembeli berikutnya? (y/n): ").lower()
    if pembeli_lagi == 'n':
        print("Program kasir selesai.")
        break
