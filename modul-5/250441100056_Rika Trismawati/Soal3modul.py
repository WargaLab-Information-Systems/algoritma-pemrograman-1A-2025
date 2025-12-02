
nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (manager/staff): ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

# Function untuk menghitung gaji
def hitung_gaji(nama, jabatan, gaji_pokok):

    pajak = 0.05 * gaji_pokok

    # Tentukan tunjangan sesuai jabatan
    if jabatan == "manager":
        tunjangan = 0.1 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0  # Kalau jabatan lain, tunjangan 0

    # Hitung gaji bersih
    gaji_bersih = gaji_pokok + tunjangan - pajak 

    # Tampilkan hasil
    print("\n=== HASIL PERHITUNGAN GAJI ===")
    print("Nama Karyawan :", nama)
    print("Jabatan       :", jabatan)
    print("Gaji Pokok    : Rp", gaji_pokok)
    print("Pajak (5%)    : Rp", pajak)
    print("Tunjangan     : Rp", tunjangan)
    print("Gaji Bersih   : Rp", gaji_bersih)

# Panggil function
hitung_gaji(nama, jabatan, gaji_pokok)