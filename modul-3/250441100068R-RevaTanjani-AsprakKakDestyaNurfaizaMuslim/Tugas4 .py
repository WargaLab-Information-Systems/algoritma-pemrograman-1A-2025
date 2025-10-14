ulang = "y"

while ulang == "y":
    nama = input("Masukkan nama pembeli: ")
    total = 0

    beli_lagi = "y"
    while beli_lagi == "y":
        barang = input("Nama barang: ")
        harga = int(input("Harga barang: "))
        total += harga
        beli_lagi = input("Apakah ingin menambah barang lagi? (y/n): ")

    print("======================")
    print("Nama pembeli:", nama)
    print("Total harga:", total)
    print("Terima kasih telah berbelanja di IndoMei")

    ulang = input("Apakah ada pembeli berikutnya? (y/n): ")