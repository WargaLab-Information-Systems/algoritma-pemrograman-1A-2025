def hitung_pajak(gaji_pokok):
    return 0.05 * gaji_pokok

def hitung_tunjangan(jabatan, gaji_pokok):
    if jabatan == "manager":
        return 0.10 * gaji_pokok
    elif jabatan == "staff":
        return 0.05 * gaji_pokok
    else:
        return 0

def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = hitung_pajak(gaji_pokok)
    tunjangan = hitung_tunjangan(jabatan, gaji_pokok)
    
    gaji_bersih = gaji_pokok + tunjangan - pajak
    
    print("\n")
    print(f"Nama karyawan : {nama}")
    print(f"Jabatan       : {jabatan}")
    print(f"Gaji pokok    : Rp{gaji_pokok}")
    print(f"Tunjangan     : Rp{tunjangan}")
    print(f"Pajak (5%)    : Rp{pajak}")
    print(f"Gaji bersih   : Rp{gaji_bersih}")

nama = input("Masukkan nama karyawan: ").lower()
jabatan = input("Masukkan jabatan (Manager/Staff): ").lower()
gaji_pokok = int(input("Masukkan gaji pokok: "))
hitung_gaji(nama, jabatan, gaji_pokok)


