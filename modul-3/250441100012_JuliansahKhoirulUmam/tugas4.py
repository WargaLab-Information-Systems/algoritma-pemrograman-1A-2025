print("="*15," Tugas 4 Program Kasir Indomei","="*15)

while True:
    # inputan Nama Pembeli
    n = input("\nMasukkan Nama Pembeli : ").upper()

    # Variabel Pandangan 
    Barang = [] #menambahkan satu elemen ke akhir list yang sudah ada
    total = 0 
    print("\nMasukkan Daftar Barang (Ketik selesai jika Sudah)")
    #perulangan barng yang di beli dan harganya
    while True:
        b = input("Barang : ").lower()
        if b == "selesai":
            break
        h = float(input(f"Masukkan Harga {b} : Rp. "))
        Barang.append((b,h))
        total += h
        
    #outputan / struk Pembayaran 
    print("\n====","Struk Pembayaran","=====")
    print(f"Pembelian Atas Nama : {n}")
    print("-------------------------------")
    print(" Daftar Barang :")
    for item, h in Barang:
        print(f"-{item} \t Rp {h:,.0f}")
    print("-------------------------------")
    print(f"Total Seluruh Barang Yang Anda Beli Adalah : Rp{total:,.0f}")
    print("Terimaksih Telah Berbelanja Di Indomei.\n")

    #Tanya Apakah Ada Pembeli Berikutnya
    L = input("Apakah ada Pembeli Berikutnya ? (y/t) : ").lower()
    if L == "t":
        print("\nProgram Selesai. Terimakasih !!!")
        break