while True:
    nama_pembeli = input("Masukkan nama pembeli: ")

    daftar_barang = []
    daftar_harga = []

    while True:
        barang = input("Masukkan nama barang (atau ketik 'selesai' jika sudah selesai): ")
        if barang.lower() == 'selesai':
            break

        while True:
            harga = int(input(f"Masukkan harga {barang}: Rp "))
            if harga < 0:
                print(" Harga harus positif !!! Silakan masukkan lagi.")
            else:
                break

        daftar_barang.append(barang)
        daftar_harga.append(harga)

    print("\nStruk Pembelian IndoMei")
    print("Nama Pembeli:", nama_pembeli)
    print("Daftar Barang:")

    total_harga = 0
    for barang, harga in zip(daftar_barang, daftar_harga):
        print(f"- {barang}: Rp {harga}")
        total_harga += harga

    print("Total Harga: Rp", total_harga)
    print("Terima kasih telah berbelanja di IndoMei.\n")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lanjut.lower() != 'y':
        print("Program selesai.")
        break
