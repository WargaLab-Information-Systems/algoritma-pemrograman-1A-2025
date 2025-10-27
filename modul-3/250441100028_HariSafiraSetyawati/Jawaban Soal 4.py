print("=== Program Struk Pembelian IndoMei ===\n")

while True:
    nama = input("Masukkan nama pembeli: ")

    daftar_barang = []
    daftar_harga = []

    print("Masukkan nama dan harga barang (ketik 'selesai' jika sudah):")
    while True:
        barang = input("Nama barang: ")
        if barang.lower() == "selesai":
            break
        harga = float(input("Harga barang (Rp): "))
        daftar_barang.append(barang)
        daftar_harga.append(harga)

    total = sum(daftar_harga)

    print("\n===== STRUK PEMBELIAN INDO MEI =====")
    print("Nama Pembeli :", nama)
    print("------------------------------------")
    print(daftar_barang, daftar_harga)
    print("------------------------------------")

    print("Total Harga: Rp ", (total))
    print("====================================")
    print("Terima kasih telah berbelanja di IndoMei.\n")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ").lower()
    if lanjut == "n":
        print("\nProgram selesai. Semua data pembelian telah dicetak.")
        break

    print("\n")