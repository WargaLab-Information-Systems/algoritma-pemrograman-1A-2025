# SOAL 3
X = str("SOAL 3")
print(X)

def gaji (nama_karyawan, jabatan_karyawan, gaji_pokok_karyawan):

    pajak = 0.05 * gaji_pokok_karyawan

    if jabatan_karyawan.lower() == "manejer":
        tunjangan_karyawan = 0.10 * gaji_pokok_karyawan
    elif jabatan_karyawan.lower() == "staff":
        tunjangan_karyawan = 0.05 * gaji_pokok_karyawan
    else:
        tunjangan_karyawan = 0

    gaji_bersih = gaji_pokok_karyawan - pajak + tunjangan_karyawan

    print ("Hasil perhitungan gaji Perusahaan ")
    print (f"Nama karyawan: {nama_karyawan}")
    print (f"Jabatan : {jabatan_karyawan}")
    print (f"jumlah gaji pokok senilai: {gaji_pokok_karyawan}")
    print (f"Jumlah tunjangan senilai Rp: {tunjangan_karyawan}")
    print (f"Jumlah pajaknya senilai: {pajak}")
    print (f"Sehinnga diperoleh gaji bersihnya senilai Rp: {gaji_bersih}")

nama_karyawan = str(input("Silahkan masukkan nama karyawan: "))
jabatan_karyawan = str(input("Silahakn masukkan nama jabatan: "))
gaji_pokok_karyawan = float(input("Silahakan masukkan gaji pokok karyawan: "))

gaji (nama_karyawan, jabatan_karyawan, gaji_pokok_karyawan)
