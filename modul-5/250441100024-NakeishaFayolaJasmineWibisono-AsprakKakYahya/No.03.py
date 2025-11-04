def hitung_gaji (nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok
    if jabatan == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0


#gaji bersih
    gaji_bersih = gaji_pokok - pajak + tunjangan
#hasil
    print("===== RINCIAN TOTAL GAJI =====")
    print(f"Nama         : {nama}")
    print(f"Jabatan      : {jabatan}")
    print(f"Gaji Pokok   : Rp {gaji_pokok:}")
    print(f"Tunjangan    : Rp {tunjangan:}")
    print(f"Pajak PPh 5% : Rp {pajak}")
    print(f"Gaji Bersih  : Rp {gaji_bersih}")
    print("==============================")

nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (Manager / Staff): ").lower()
gaji_pokok = float(input("Masukkan gaji pokok: "))
hitung_gaji(nama, jabatan, gaji_pokok)