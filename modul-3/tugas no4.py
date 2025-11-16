print("=== Program Struk Pembelian IndoMei ===")

lanjut = "y"

while lanjut == "y":
    nama = input("Masukkan nama pembeli: ")
    jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))

    total = 0
    print("\n=== Masukkan Data Barang ===")
    for i in range(1, jumlah_barang + 1):
        print("Barang ke-", i)
        barang = input("  Nama barang : ")
        harga = int(input("  Harga barang: "))
        total = total + harga

        print("  ->", barang, "Rp", harga)
        print()

    print("===================================")
    print("          STRUK PEMBELIAN          ")
    print("===================================")
    print("Nama Pembeli :", nama)
    print("Jumlah Barang:", jumlah_barang)
    print("Total Harga  : Rp", total)
    print("Terima kasih telah berbelanja di IndoMei")
    print("===================================\n")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    print()

print("Program selesai. Semua pembeli telah dilayani.")