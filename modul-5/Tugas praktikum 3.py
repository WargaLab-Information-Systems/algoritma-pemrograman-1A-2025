# Fungsi untuk menghitung gaji bersih
def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok # PPh tetap 5%
    # Hitung tunjangan berdasarkan jabatan
    if jabatan.lower() == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan.lower() == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0  # Tidak ada tunjangan untuk jabatan lain

    # Hitung gaji bersih
    gaji_bersih = gaji_pokok + tunjangan - pajak
    # Tampilkan hasil perhitungan secara lengkap
    print(f"Nama Karyawan : {nama}")
    print(f"Jabatan       : {jabatan}")
    print(f"Gaji Pokok    : Rp{gaji_pokok}")
    print(f"Pajak (5%)    : Rp{pajak}")
    print(f"Tunjangan     : Rp{tunjangan}")
    print(f"Gaji Bersih   : Rp{gaji_bersih}")
    
nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (Manager/Staff): ")
gaji_pokok = int(input("Masukkan gaji pokok: "))
hitung_gaji(nama, jabatan, gaji_pokok) # Panggil fungsi