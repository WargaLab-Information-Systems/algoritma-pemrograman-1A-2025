def hitung_gaji(nama, jabatan, gaji):
    pajak = gaji * 0.05

    if jabatan.lower() == "manager":
        tunjangan = gaji * 0.1
    elif jabatan.lower() == "staff":
        tunjangan = gaji * 0.05
    else:
        tunjangan = 0

    gaji_bersih = gaji + tunjangan - pajak

    print("\n===================")
    print("Nama           :", nama)
    print("Jabatan        :", jabatan)
    print("Gaji Pokok     :", gaji)
    print("Tunjangan      :", tunjangan)
    print("Pajak (5%)     :", pajak)
    print("Gaji Bersih    :", gaji_bersih)
    print("====================\n")

nama = input("Nama : ")
jabatan= input("Jabatan (Manager/Staff): ")
gaji = input("Gaji pokok: ")

hitung_gaji(nama, jabatan, int(gaji))
