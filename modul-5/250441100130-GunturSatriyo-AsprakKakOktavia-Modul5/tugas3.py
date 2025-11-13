def hitung_gaji_bersih(nama, jabatan, gajipokok):
    pajak = 0.05 * gajipokok
    
    if jabatan == "manager":
        tunjangan = 0.10 * gajipokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gajipokok
    else:
        tunjangan = 0
    
    gaji_bersih = gajipokok - pajak + tunjangan
    
    print("Nama Karyawan: ", nama)
    print(f"Gaji Pokok: Rp{gajipokok:,}")
    print(f"Pajak (5%): Rp{pajak:,}")
    print(f"Tunjangan: Rp{tunjangan:,}")
    print(f"Gaji Bersih: Rp{gaji_bersih:,}")
   

nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan karyawan (Manager/Staff): ")
gajipokok = int(input("Masukkan gaji pokok: "))

hitung_gaji_bersih(nama, jabatan, gajipokok)