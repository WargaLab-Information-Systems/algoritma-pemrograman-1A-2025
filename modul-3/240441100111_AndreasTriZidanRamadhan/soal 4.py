while True:
    nama = input("Masukkan nama Anda: ")
    daftar_barang = int(input("Masukkan jumlah barang yang dibeli: "))
    total_barang = ""
    total = 0

    for i in range(daftar_barang):
        nama_barang = input("Masukkan nama barang: ")
        harga = int(input("Masukkan harga barang: "))

        total_barang += nama_barang + ": " + str(harga)+" ,"
        total += harga

    print("Nama:", nama)
    print("Daftar barang:", total_barang)
    print("Total harga:", total)
    print("Terima kasih telah berbelanja di IndoMei.")

    ulang = input("Apakah Anda ingin mengulang? (y/n): ").lower()
    if ulang != 'y':
        break