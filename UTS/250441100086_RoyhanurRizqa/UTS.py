while True:
    print("Kasir Toko Sembako “Maju Jaya” ")
    print("daftar barang ")
    print("1. beras = Rp12000/kg")
    print("2. gula = Rp14000/kg")
    print("3. minyak = Rp20000/liter")
    beras=12000
    gula=14000
    minyak=20000
    hargaberas=0
    hargagula=0
    hargaminyak=0
    totalakhir=0
    # barang=[]
    # banyak_jenis=int(input("masukkan jenis barang yang ingin dibeli : "))
    # for x in range(1,banyak_jenis):
    #     baranga=input("masukkan nama barang yang dibeli :")
    #     jumlahb=("masukkan banyak barang")
    
    # daftar=barang.append((baranga,jumlahb))

    banyak_jenis=int(input("masukkan banyak jenis barang yang ingin dibeli : "))
    for x in range (1,banyak_jenis+1):
        namabarang=input(f"masukkan no barang ke-{x} dari daftar yang ingin dibeli : ")
        jumlahdibeli=input("masukkan jumlah yang ingin dibeli")
        if namabarang==1:
            hargaberas=beras*jumlahdibeli
        elif namabarang == 2:
            hargagula == gula*jumlahdibeli
        elif namabarang == 3:
            hargaminyak == minyak*jumlahdibeli
        else:
            pass
    total=hargaberas + hargagula+hargaminyak

    if total > 200000 :
        hargadiskon=total*0.15
    elif total > 100000:
        hargadiskon=total*0.1
    else:
        hargadiskon=total

    member=input("apakah memiliki member card (y/n)").lower()
    if member == "y":
        totalakhir=hargadiskon*0.05
        
    print("total seluruhnya adalah : Rp",totalakhir)

    lanjut=("apakah ada pelanggan selanjutnya(y/n):").lower()
    if lanjut =="n":
        break