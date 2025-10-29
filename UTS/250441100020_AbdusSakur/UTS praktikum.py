adaLagi ="y"
while adaLagi == "y":
    beras = 12000
    gula = 14000
    minyak = 20000
    memberCard = 0.05


    ada = "y"
    while ada =="y":
        n = (input("masukan barang: "))
        h = int(input("masukkan harga: "))
        j = int(input("jumlah: "))
        for i in ada:
            harga = h * j
            print(harga)
        total += harga
    l = print(input("apakah ada barang lagi, tekan(y,n): ")).lower()
    if l == "y":
       print(ada)
    else:
        break

    print("subtotal belanjaan adalah: ",total)
    if total >= 100000 and total<= 150000:
        total * 0.10
        print(total)
    elif total <200000 and total>150000:
        print(total)
    else:
        if total >= 200000:
            total * 0.15
            print(total)


lagi=print(input("apakah ada pembeli lagi (y,n)")).lower()
if lagi == "y":
    print(adaLagi)