def gaji_bersih(nama,jabatan,gaji_pokok):
    if jabatan.lower() == "manager":
        tunjangan = gaji_pokok * 0.10
    elif jabatan.lower() == "staff":
        tunjangan = gaji_pokok * 0.05
    else:
        tunjangan = 0
    
    pajak = gaji_pokok * 0.05
    gaji_bersih = gaji_pokok + tunjangan - pajak
    
    print(f"Nama Karyawan: {nama}")
    print(f"Jabatan: {jabatan}")
    print(f"Gaji Pokok: Rp{gaji_pokok}")
    print(f"Tunjangan: Rp{tunjangan}")
    print(f"Pajak PPh (5%): Rp{pajak}")
    print(f"Gaji Bersih: Rp{gaji_bersih}")
    return gaji_bersih

nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (Manager/Staff): ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

if gaji_pokok < 0:
    print("Gaji tidak boleh Negatif")
    exit()
    
gaji_bersih(nama, jabatan, gaji_pokok)