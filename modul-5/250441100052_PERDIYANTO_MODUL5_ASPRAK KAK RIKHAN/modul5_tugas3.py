def hitung_gaji(nama, jabatan, gaji_pokok):

    if jabatan.lower() == "manager":
        tunjangan = 0.1 * gaji_pokok
    elif jabatan.lower() == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0

    pph = 0.05 * gaji_pokok

    gaji_bersih = gaji_pokok - pph + tunjangan

    print("\n=== RINCIAN GAJI KARYAWAN ===")
    print(f"Nama Karyawan      : {nama}")
    print(f"Jabatan            : {jabatan}")
    print(f"Gaji Pokok         : Rp {gaji_pokok}")
    print(f"Tunjangan          : Rp {tunjangan}")
    print(f"PPH (5%)           : Rp {pph}")
    print("-" * 40)
    print(f"Gaji Bersih Bulanan: Rp {gaji_bersih}")
    print("===============================")


nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (Manager/Staff): ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

hitung_gaji(nama, jabatan, gaji_pokok)
