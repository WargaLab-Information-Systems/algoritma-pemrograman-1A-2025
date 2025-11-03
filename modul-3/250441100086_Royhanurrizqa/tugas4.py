while True :
    print("program struk pembelian indomei")
    nama=str(input("masukkan nama pembeli : "))

    daftar=[]
    total_harga=0

    while True:
        barang=str(input("masukkan nama barang(ketik 'cukup' apabila sudah selesai) :")).lower()
        if barang == "cukup":
            break
        harga=int(input(f"masukkan harga{barang}:Rp"))
        daftar.append((barang,harga))
        total_harga += harga
    
    print("======== STRUK BELANJA INDOMEI ========")
    print("nama pembeli : ",nama)
    print("daftar barang :")
    for namabarang,rupiah in daftar:
        print("-",namabarang," :Rp ",rupiah)
    print("total harganya :Rp ",total_harga)
    print("========================================")
    print("Terima kasih telah berbelanja di indomei")
    print("========================================")

    lanjut=str(input("apakah ada pembeli berikutnya (y/n) :")).lower()
    if lanjut == "n":
        print("program selesai.terima kasih")
        break