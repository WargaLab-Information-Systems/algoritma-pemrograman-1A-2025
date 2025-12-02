# Menghitung gaji karyawan dengan potongan pajak dan tunjangan
def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    pph = 0.05 * gaji_pokok
    tunjangan = {"manager": 0.10, "staff": 0.05}.get(jabatan.lower(), 0) * gaji_pokok
    gaji_bersih = gaji_pokok - pph + tunjangan
    return(f"""
--- RINCIAN GAJI ---
Nama        : {nama}
Jabatan     : {jabatan}
Gaji Pokok  : Rp {gaji_pokok:,.2f}
PPh (5%)    : Rp {pph:,.2f}
Tunjangan   : Rp {tunjangan:,.2f}
-------------------------
Gaji Bersih : Rp {gaji_bersih:,.2f}
-------------------------
""")

# Input nama (ulang jika angka)
nama = ""
while nama == "":
    nama_input = input("Masukkan nama karyawan: ")
    try:
        float(nama_input)
        print("Input tidak valid! Nama tidak boleh berupa angka. Coba lagi.")
    except ValueError:
        nama = nama_input

# Input jabatan (ulang jika angka)
jabatan = ""
while jabatan == "":
    jabatan_input = input("Masukkan jabatan (Manager/Staff): ")
    try:
        float(jabatan_input)
        print("Input tidak valid! Jabatan tidak boleh berupa angka. Coba lagi.")
    except ValueError:
        jabatan = jabatan_input

# Input gaji (ulang jika bukan angka atau negatif)
gaji_pokok = -1
while gaji_pokok < 0:
    try:
        gaji_pokok = float(input("Masukkan gaji pokok: "))
        if gaji_pokok < 0:
            print("Gaji pokok tidak boleh negatif, coba lagi.")
    except ValueError:
        print("Input tidak valid! Masukkan angka yang benar.")
        gaji_pokok = -1  # ulang lagi

# Hitung gaji bersih
print(hitung_gaji_bersih(nama, jabatan, gaji_pokok))