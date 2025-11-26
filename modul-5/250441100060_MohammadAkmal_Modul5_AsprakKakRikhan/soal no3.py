def hitung_gaji(nama, jabatan, gaji_pokok):
    if jabatan.lower() == "manager":
        tunjangan = gaji_pokok * 0.10
    elif jabatan.lower() == "staff":
        tunjangan = gaji_pokok * 0.05
    else:
        tunjangan = 0

    pajak = gaji_pokok * 0.05
    gaji_bersih = gaji_pokok + tunjangan - pajak

    print("=== Hasil Perhitungan Gaji ===")
    print("Nama       :", nama)
    print("Jabatan    :", jabatan)
    print("Gaji Pokok :", gaji_pokok)
    print("Tunjangan  :", tunjangan)
    print("Pajak      :", pajak)
    print("Gaji Bersih:", gaji_bersih)

nm = input("Nama karyawan : ")
jb = input("Jabatan (Manager/Staff): ")
gp = float(input("Gaji pokok : "))

hitung_gaji(nm, jb, gp)