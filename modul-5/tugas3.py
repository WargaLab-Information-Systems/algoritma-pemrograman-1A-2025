def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok  # PPh 5%
    
    if jabatan.lower() == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan.lower() == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0
    
    gaji_bersih = gaji_pokok - pajak + tunjangan
    
    print(f"Nama Karyawan: {nama}")
    print(f"Jabatan: {jabatan}")
    print(f"Gaji Pokok: Rp{gaji_pokok:,}")
    print(f"Pajak (5%): Rp{pajak:,}")
    print(f"Tunjangan: Rp{tunjangan:,}")
    print(f"Gaji Bersih: Rp{gaji_bersih:,}")
    return gaji_bersih

# Contoh pemakaian fungsi
nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan karyawan (Manager/Staff): ")
gaji_pokok = int(input("Masukkan gaji pokok: "))

hitung_gaji_bersih(nama, jabatan, gaji_pokok)
