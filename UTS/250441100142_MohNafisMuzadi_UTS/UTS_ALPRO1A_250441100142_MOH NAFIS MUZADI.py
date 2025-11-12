i = 0
diskon = 0
print("Toko Sembako Maju Jaya")
print("List harga barang yang tersedia")
print("Beras Rp. 12000/kg")
print("Gula Rp. 14000/kg")
print("Minyak Rp. 20000/liter")

while True :
    while True :
        i += 1
        barang = input(f"Masukkan barang belanjaan ke-{i} :")
        harga = float(input("Masukkan harga barang :"))
        print("Input 0 jika tidak ada belanjaan lagi")
        if barang == 0 :
            break
        vip = input("Apakah anda mempunya member? (y/n) :").lower
        total = harga
        print(total)
        if vip == "y":
            if total >= 200000 :
                diskon = total - 0.20
            elif total >= 150000 :
                diskon = total - 0.15
            elif total >= 100000 :
                diskon = total - 0.15
            else :
                diskon = diskon
        else :
            if total >= 200000 :
                diskon = total - 0.15
            elif total >= 150000 :
                diskon = total - 0.10
            elif total >= 100000 :
                diskon = total - 0.10
            else :
                diskon = diskon
                
        print("Harga akhir :  ", total - diskon )
        
    stop = input("Apakah ada pelanggan berikutnya? (y/n)").lower
    if stop == "n" :
        stop = False
    else:
        stop = True