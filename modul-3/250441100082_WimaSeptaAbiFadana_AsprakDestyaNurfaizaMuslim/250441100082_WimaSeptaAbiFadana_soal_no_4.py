ulang = "y"

while ulang == "y":
    nama_pembeli = input("Masukkan nama pembeli : ")

    daftar_barang = []
    daftar_jumlah = []
    daftar_harga = []

    total = 0

    while True:
        barang = input("Masukkan barang yang dibeli (ketik selesai jika sudah): ")
        if barang.lower() == "selesai":
            break

        jumlah_barang = int(input("Berapa jumlahnya: "))
        harga = int(input("Masukkan harga per barangnya (Rp): "))

        daftar_barang.append(barang)
        daftar_jumlah.append(jumlah_barang)
        daftar_harga.append(harga * jumlah_barang)

        total += harga * jumlah_barang

    print("===== STRUK PEMBELIAN DI INDO MEI =====")
    print("Nama pembeli:", nama_pembeli)
    print("----------------------------------------")
    for i in range(len(daftar_barang)):
        print("Barang:", daftar_barang[i], ", Jumlah:", daftar_jumlah[i], ", Total harga: Rp", daftar_harga[i])
    print("----------------------------------------")
    print("Total seluruh belanja: Rp", total)
    print("===== Terima kasih telah berbelanja di IndoMei =====")

    ulang = input("Apakah ada pembeli berikutnya? (y/n): ").lower()
