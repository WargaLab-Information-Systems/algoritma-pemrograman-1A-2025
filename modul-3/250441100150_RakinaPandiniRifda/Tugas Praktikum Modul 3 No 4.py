lanjut = "y"

while lanjut == "y":
    nama = input("Nama pembeli: ")

    barang = {}
    selesai = ""
    
    while selesai != "selesai":
        nama_barang = input("Nama barang (ketik 'selesai' or 'SELESAI' jika sudah): ") 
        
        if nama_barang == "selesai" or nama_barang == "SELESAI": 
            selesai = "selesai"
        else:
            try:
                harga = float(input(f"Harga {nama_barang}: "))
                barang[nama_barang] = harga
            except ValueError:
                print("Harga harus berupa angka. Silakan masukkan lagi.")

    print("\n=== Struk IndoMei ===")
    print(f"Pembeli: {nama}")

    total_harga = 0 
    
    for nama_barang in barang:
        harga = barang[nama_barang] 
        
        print(f"{nama_barang:<30} Rp{harga:>10,.0f}")
        total_harga += harga

    print("----------------------")
    print(f"Total: Rp{total_harga:,.0f}")
    print("Terima kasih telah berbelanja di IndoMei!")

    lanjut_input = input("Apakah ada pembeli berikutnya? (y/n): ")