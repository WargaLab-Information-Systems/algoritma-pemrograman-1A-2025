jenis_barang = []
total_belanja = 0
a = 12000
b = 14000
c = 20000

diskon = 0
setelah_diskon = 0
diskon_member = 0
dMember = 0


while True:
    
    while True:
        barang = input("Pilih barang yang dibeli : A. Beras : Rp.12000/kg | B. Gula : Rp. 14.000/kg | C. Minyak Rp. 20.000/liter (selesai untuk mengakhiri) : ").lower()
        if barang == "selesai":
            break
        if barang == "a":
            total_belanja += a
        elif barang == "b":
            total_belanja += b
        elif barang == "c":
            total_belanja += c
            
    if total_belanja >= 200000:
        diskon = 0.15
    elif total_belanja >= 100000:
        diskon = 0.10
    
    setelah_diskon = total_belanja - (total_belanja * diskon)
    print(f"Jumlah Harga belanjaan : Rp{total_belanja} ")
    print("dapat diskon : ", int(diskon*100) , "%")
    print(f"Harga setelah_diskon adalah : Rp{setelah_diskon}")
    if setelah_diskon > 150000:
        diskon = 0.10
        print("anda mendapat diskon lagi 10%")
        setelah_diskon = total_belanja - (total_belanja * diskon)
        print(f"Harga setelah lagi diskon adalah : Rp{setelah_diskon}")

    member = input("apakah memiliki kartu member : (ya/tidak) ").lower()
    if member == "ya":
        dMember = 0.05
    diskon_member = setelah_diskon - (setelah_diskon * dMember)
    print(f"Harga final member adalah : Rp{diskon_member}")
    ulang = input("ada pelanggan lain (y/n) : ")
    if ulang != "y":
        break