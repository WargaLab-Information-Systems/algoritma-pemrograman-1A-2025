def hitung(nama, jabatan, gaji):
    pph = gaji * 0.05

    if jabatan == "manager":
        tunjangan = gaji * 0.10
    elif jabatan == "karyawan":
        tunjangan = gaji * 0.05
    else:
        tunjangan = 0

    gaji1 = gaji - pph + tunjangan 

    print(f"Nama Karyawan      : {nama}")
    print(f"Jabatan            : {jabatan}")
    print(f"Gaji Pokok         : Rp{gaji:,.2f}")
    print(f"Tunjangan Jabatan  : Rp{tunjangan:,.2f}")
    print(f"PPh (5%)           : Rp{pph:,.2f}")
    print(f"Gaji Bersih        : Rp{gaji1:,.2f}")

nama = input("Masukkan nama karyawan : ")
jabatan = input("Masukkan jabatan (Manager/Karyawan) : ").lower()
while jabatan not in ["manager", "karyawan"]:
    jabatan = input("Jabatan hanya ada dua pilihan (Manager/Karyawan). Silahkan memasukkan lagi : ").lower()
gaji = float(input("Masukkan gaji pokok : "))


hitung(nama, jabatan, gaji) 