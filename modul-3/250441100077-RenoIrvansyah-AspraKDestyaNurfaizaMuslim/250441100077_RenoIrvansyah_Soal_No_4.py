while True:
    nama_pembeli = input("Masukkan nama pembeli: ")
    daftar_belanja = []
    total_harga = 0

    while True:
        nama_barang = input("Masukkan nama barang (atau ketik 'selesai' untuk mengakhiri): ")
        if nama_barang.lower() == 'selesai':
            break
        harga = int(input(f"Masukkan harga {nama_barang}: "))
        daftar_belanja.append((nama_barang, harga))
        total_harga += harga

    print("=" * 30)
    print("Struk Belanja")
    print(f"Nama Pembeli: {nama_pembeli}")
    print("Daftar Barang:")
    for barang, harga in daftar_belanja:
        print(f"-> {barang}: Rp {harga}")
    print(f"Total Harga: Rp {total_harga}")
    print("=" * 30)
    print("Terima kasih telah berbelanja di IndoMei.")
    print("=" * 30)
    
    ulang = input("Apakah ada pembeli berikutnya? (y/n): ")
    if ulang.lower() != 'y':
        break