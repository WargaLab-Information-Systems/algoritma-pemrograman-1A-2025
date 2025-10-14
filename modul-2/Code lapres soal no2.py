harga_normal = 50000

usia = int(input("Masukkan usia anda: "))
if usia < 12:
    diskon = 0.5
    hari = input("Masukkan hari: ")
    harga_akhir = harga_normal - (harga_normal * diskon)

    print("\n=== Hasil Perhitungan Harga Tiket ===")
    print("Harga tiket normal      : Rp",(harga_normal))
    print("Diskon yang diterapkan  :", int(diskon * 100),"%")
    print("Total yang harus dibayar: Rp",int(harga_akhir))
elif usia < 16:
    hari = input("Masukkan hari: ")
    if hari == "selasa":
        diskon = 0.2
    else:
        diskon = 0
    harga_akhir = harga_normal - (harga_normal * diskon)

    print("\n=== Hasil Perhitungan Harga Tiket ===")
    print("Harga tiket normal      : Rp",(harga_normal))
    print("Diskon yang diterapkan  :", int(diskon * 100),"%")
    print("Total yang harus dibayar: Rp",int(harga_akhir))
else:   
    pelajar = input("Apakah Anda pelajar SMA? (ya/tidak): ")
    kartu = input("Apakah Anda membawa kartu pelajar? (ya/tidak): ")
    if kartu == "ya":
        diskon = 0.30
        harga_akhir = harga_normal - (harga_normal * diskon)

        print("\n=== Hasil Perhitungan Harga Tiket ===")
        print("Harga tiket normal      : Rp",(harga_normal))
        print("Diskon yang diterapkan  :", int(diskon * 100),"%")
        print("Total yang harus dibayar: Rp",int(harga_akhir))
    else :
        diskon = 0
        harga_akhir = harga_normal - (harga_normal * diskon)

        print("\n=== Hasil Perhitungan Harga Tiket ===")
        print("Harga tiket normal      : Rp",(harga_normal))
        print("Diskon yang diterapkan  :", int(diskon * 100),"%")
        print("Total yang harus dibayar: Rp",int(harga_akhir))