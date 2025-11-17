kupon = {"DISC": 10, "HEMAT": 20}

while True:
    print("1. Lihat kupon")
    print("2. Transaksi")
    print("3. Keluar")
    p = input("Pilih menu 1-3: ")

    if p == "1":
        if not kupon: print("Tidak ada kupon. ")
        for k, v in kupon.items(): print(k, "-", v, "%")
    elif p == "2":
        total = float(input("Total belanja: "))
        kode = input("Kode kupon: ")

        if kode not in kupon:
            print("Kupon tidak valid / sudah dipakai. ")
        else:
            d = kupon[kode]
            bayar = total - (total * d/100)
            print("Diskon: ", d, "%")
            print("Total bayar: ", bayar)
            del kupon[kode]
            print("kupon dihapus (tidak bisa dipakai lagi). ")
    elif p == "3":
        break 