beras = 12000
gula = 14000
minyak = 20000
banyak = int(input("masukan banyak barang yang mau di beli"))
card = input("apakah memiliki member card (y/n)")
print("1. beras ")
print("2. gula ")
print("3. minyak ")
while True:
    diskon1 = 0
    subtotal = 0
    bayar = 0
    total = 0
    diskon2 = 0 
    for i in range(1, banyak+1):
        nama = int(input("masukan nomor barang "))
        jumlah = int(input("masukkan jumlah barang per Kg"))
        if nama == 1:
            total = beras * jumlah
            subtotal += total
            if total > 150000:
                diskon1 += 0.1
        elif nama == 2:
            total = gula * jumlah
            subtotal += total
            if total > 150000:
                diskon1 += 0.1
        elif nama == 3:
            total = minyak * jumlah
            subtotal += total
            if total > 150000:
                diskon1 += 0.1
        else:
            print("tidak ada barang di nomor itu")
    if card.lower() == "y":
        diskon3 = 0.05
        if subtotal > 100000 and subtotal < 200000:
            diskon2 = subtotal*0.1
            totaldiskon = diskon1+diskon2
            bayar = subtotal - totaldiskon
            print(f"total bayar {bayar} setelah dapat diskon {totaldiskon}")
        elif subtotal > 200000:
            diskon2 = subtotal*0.15
            totaldiskon = diskon1+diskon2
            bayar = subtotal - totaldiskon
            print(f"total bayar {bayar} setelah dapat diskon {totaldiskon}")
        else:
            totaldiskon = diskon1
            bayar = subtotal - diskon1
            print(f"total bayar {bayar} setelah dapat diskon {totaldiskon} ")
    else:
        if subtotal > 100000 and subtotal < 200000:
            diskon2 = subtotal*0.1
            totaldiskon = diskon1+diskon2
            bayar = subtotal - totaldiskon
            print(f"total bayar {bayar} setelah dapat diskon {totaldiskon}")
        elif subtotal > 200000:
            diskon2 = subtotal*0.15
            totaldiskon = diskon1+diskon2
            bayar = subtotal - totaldiskon
            print(f"total bayar {bayar} setelah dapat diskon {totaldiskon}")
        else:
            totaldiskon = diskon1
            bayar = subtotal - diskon1
            print(f"total bayar {bayar} setelah dapat diskon {totaldiskon} ")
    
    lanjut = input("apakah ada pembeli selanjutnya  (y/n)")
    if lanjut.lower() == "n":
        break


