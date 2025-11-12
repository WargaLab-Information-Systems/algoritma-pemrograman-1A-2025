while True:
    nama = input("Masukkan nama anda : ")
    jumlahproduk = int(input("Masukkan jumlah barang yang di beli : "))
    
    produk = []
    harga = 0
    
    for i in range(jumlahproduk):
        print(f"\nbarang ke-{i+1}")
        namaproduk = input("Nama Produk yang anda beli : ") 
        hargaproduk = float(input("Harga produk : "))
        
        produk.append((namaproduk, hargaproduk))
        harga += hargaproduk
        
    print("\n======= STRUK BELANJA =======")
    print(f"Nama Pembeli : {nama}")
    print("-------------------------------")
    for produk1, harga1 in produk :
        print(f"{produk1:15} Rp {harga1:,.2f}")
    print("-------------------------------")
    print(f"Total Harga : Rp {harga:,.2f}")
    print("==== TERIMAKASIH ====\n")
    
    lanjut = input("Apakah ada pembeli berikutnya? (y/n)").lower()
    if lanjut != "y" :
        print("\nProgram selesai. Terima kasih'u'")
        break
    