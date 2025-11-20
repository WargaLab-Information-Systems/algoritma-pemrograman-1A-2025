def gaji(nama, jabatan, gaji_pokok):

    pajak = 0.05 * gaji_pokok
    nama = nama
    jabatan = jabatan
    gaji_pokok = gaji_pokok

    if jabatan == "manager":
        tunjangan = 0.1 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0

    total_gaji = gaji_pokok - pajak + tunjangan

    return nama, jabatan, pajak, tunjangan, total_gaji

input_nama = input("Masukkan Nama Karyawan: ")
input_jabatan = input("Masukkan Jabatan (Manager/Staff): ").lower()
input_gaji_pokok = float(input("Masukkan Gaji Pokok: "))

nama, jabatan, pajak, tunjangan, total_gaji = gaji(input_nama, input_jabatan, input_gaji_pokok)

print(f"Nama Karyawan    : {nama}")
print(f"Jabatan          : {jabatan}")
print(f"Gaji Pokok       : Rp {input_gaji_pokok}")
print(f"Pajak            : Rp {pajak}")
print(f"Tunjangan        : Rp {tunjangan}")
print(f"Total Gaji       : Rp {total_gaji}")