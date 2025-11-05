ulang = "y"

while ulang == "y":
    nama = input("Masukkan nama pembeli: ")
    total = 0
    jumlah = 0
    daftarBarang = []

    ada_barang = "y"
    while ada_barang == "y":
        barang = input("nama barang: ")
        harga = int(input("Harga barang: "))
        daftarBarang.append((barang, harga))
        total = total + harga

        adaBarang = input("apakah ada barang lagi? (y/n): ").lower()
        if adaBarang == "n":
            break


    print("nama pembeli: ", nama)
    print("daftar barang: ")
    for barang, harga in daftarBarang:
        print(f"{barang} Rp {harga}")
    print("total harga: Rp",total)
    print("Terima kasih telah berbelanja di IndoMei")

    ulang = input("Apakah ada pembeli berikutnya? (y/n): ")