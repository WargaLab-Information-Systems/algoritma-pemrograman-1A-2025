total_belanja = 0
pembelian =0
member_card = 0
pelanggan = 1
harga_barang = 0

print("="*50)
print("             Toko Sembako Maju Jaya          ")
print("-"*50)
print("Silahkan masukkan belanjaan anda")

barang = []
while barang == 1:
    for i in range(1, 0):
        barang = 1
        barang = int(input("Barang belanja: ", barang))
    if pembelian > 1:
        pembelian = 1
        if harga_barang > 1:
            barang = int(input("Harga barang: ", harga_barang))
            if total_belanja > 100.000:
                diskon = 10
            if total_belanja > 200.000:
                diskon = 15
            elif diskon == 10:
                if total_belanja == 150.000:
                    diskon = 0
                    print("Tidak berlaku kelipatan")
                    continue
                if pelanggan == member_card == 1:
                    diskon = 5 
                    pelanggan = ("jika memiliki member card, maka mendapatkan (diskon tambahan 5%)")
        else :
            print("Program selesai")