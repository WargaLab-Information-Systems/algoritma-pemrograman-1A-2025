while True:
    nama_pembeli = input("Masukkan nama pembeli: ")
    total = 0
    barang_list = []

    while True:
        nama_barang = input("Masukkan nama barang (ketik 'selesai' untuk berhenti): ")
        if nama_barang.lower() == "selesai":
            break
        
        harga_input = input("Masukkan harga barang: Rp ")
        harga_input = harga_input.replace(".", "").replace(",", "")
        harga = int(harga_input)

        barang_list.append((nama_barang, harga))
        total += harga

    # cetak struk
    print("===== Struk Pembelian IndoMei =====")
    print("Nama Pembeli :", nama_pembeli)
    for barang, harga in barang_list:
        print(f"- {barang}: Rp{harga:,}".replace(",", "."))
    print(f"Total harga : Rp{total:,}".replace(",", "."))
    print("Terima kasih telah berbelanja di IndoMei")

    lanjut = input("Apakah ada pembeli berikutnya? (ya/tidak): ")
    if lanjut.lower() != 'ya':
        break