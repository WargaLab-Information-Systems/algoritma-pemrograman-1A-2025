nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (manager/staff): ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

# Hitung tunjangan berdasarkan jabatan
if jabatan == "manager":
    tunjangan = 0.1 * gaji_pokok
elif jabatan == "staff":
    tunjangan = 0.05 * gaji_pokok
else:
    tunjangan = 0

# Hitung pajak 5% dari gaji pokok
pajak = 0.05 * gaji_pokok

# Hitung gaji bersih
gaji_bersih = gaji_pokok + tunjangan - pajak

# Tampilkan hasil
print("=== Rincian Gaji ===")
print(f"Nama        : {nama}")
print(f"Jabatan     : {jabatan}")
print(f"Gaji Pokok  : Rp {gaji_pokok:}")
print(f"Tunjangan   : Rp {tunjangan:}")
print(f"Pajak PPh 5%: Rp {pajak:}")
print(f"Gaji Bersih : Rp {gaji_bersih:}")
print("====================")