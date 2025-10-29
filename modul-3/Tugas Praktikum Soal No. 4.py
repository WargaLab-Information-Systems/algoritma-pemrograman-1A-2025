while True:
    print("=== IndoMei ===")
    nama = input("Nama pembeli: ")

    daftar_barang = []     
    daftar_harga = []      
    total = 0             
    jumlah_barang = 0   
    
    while True:
        barang = input("Nama barang (atau ketik '-' untuk selesai): ")
        if barang == '-':
            break
        harga = int(input(f"Harga {barang}: "))

        daftar_barang += [barang]
        daftar_harga += [harga]

        total += harga
        jumlah_barang += 1  

    print("\n=== Struk Pembelian IndoMei ===")
    print(f"Nama Pembeli: {nama}")
    print("Daftar Barang:")

    i = 0
    while i < jumlah_barang:
        print(f"{i+1}. {daftar_barang[i]} - Rp{daftar_harga[i]}")
        i += 1

    print(f"Total: Rp{total}")
    print("Terima kasih telah berbelanja di IndoMei.\n")

    lanjut = input("Apakah ada pembeli berikutnya? (ya/tidak): ")
    if lanjut != "ya":
        break 