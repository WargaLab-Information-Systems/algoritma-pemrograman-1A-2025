while True:
    nama = input("Masukkan nama pembeli: ")
    jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
    
    total = 0
    daftar_barang = []
    
    for i in range(jumlah_barang):
        nama_barang = input(f"Nama barang ke-{i+1}: ")
        harga = int(input(f"Harga {nama_barang}: "))
        daftar_barang.append((nama_barang, harga))
        total += harga
        
    print("Nama pembeli:", nama)
    for barang, harga in daftar_barang:
        print(f"{barang} - Rp{harga}")
    print("Total harga: Rp", total)
    print("Terima kasih telah berbelanja di IndoMei.")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lanjut.lower() == 'n':
        break