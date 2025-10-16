while True:
    nama = input("Masukkan nama pembeli: ")
    jumlah_barang = int(input("Berapa banyak barang yang dibeli? "))
    total = 0

    for i in range(jumlah_barang):
        barang = input(f"Nama barang ke-{i+1}: ")
        harga = float(input(f"Harga {barang}: Rp "))
        total = total + harga

    print("\n==== STRUK PEMBELIAN INDOMIE ====")
    print(f"Total harga: Rp {total:.2f}")
    print("Terima kasih telah berbelanja di Indomie!\n")
    ulang = input("Apakah anda pembeli berikutnya? (y/n): ").lower
    if ulang != "y":
        print("Program selesai, Terimakasih!")
        break     