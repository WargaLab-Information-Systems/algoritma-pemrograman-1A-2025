# Program menghitung gaji bersih bulanan karyawan

def hitung_gaji_bersih(nama, jabatan, gaji_pokok):

    # Hitung pajak 5%
    pajak = 0.05 * gaji_pokok

    # Hitung tunjangan sesuai jabatan
    if jabatan.lower() == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan.lower() == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0  # Jika jabatan lain, tidak ada tunjangan

    # Hitung gaji bersih
    gaji_bersih = gaji_pokok - pajak + tunjangan

    # Tampilkan hasil perhitungan lengkap
    print("\n===== RINCIAN GAJI KARYAWAN =====")
    print(f"Nama Karyawan   : {nama}")
    print(f"Jabatan         : {jabatan}")
    print(f"Gaji Pokok      : Rp{gaji_pokok:,.2f}")
    print(f"Pajak (5%)      : Rp{pajak:,.2f}")
    print(f"Tunjangan       : Rp{tunjangan:,.2f}")
    print(f"Gaji Bersih     : Rp{gaji_bersih:,.2f}")
    print("==================================")

# Program utama
nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (Manager/Staff): ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

hitung_gaji_bersih(nama, jabatan, gaji_pokok)
