while True:
    print("===SELAMAT DATANG DI INDO MEI===")
    nama = input("Nama pembeli: ")
    total = 0
    
    banyak = int(input("Berapa banyak barang?"))
    for i in range(banyak):
        barang = input(f"Nama barang ke-{i+1}:")
        harga = int(input("Harga barang: "))
        total += harga
        
    print("=== STRUK BELANJA ===")
    print("Nama pembeli :", nama)
    print("Total Belanja: Rp", total)
    print("Terima kasih telah berbelanja di INDO MEI!")
    print("----------------------------")
    
    ulang = input("apakah ada pembeli berikutnya?: ")
    if ulang.lower() != "ya" :
        print("Program selesai. Terima kasih!")
        break