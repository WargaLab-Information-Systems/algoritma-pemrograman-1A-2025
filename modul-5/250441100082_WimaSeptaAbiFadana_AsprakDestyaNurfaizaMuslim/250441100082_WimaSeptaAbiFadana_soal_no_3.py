def menghitung_gaji():
    nama = str(input("masukan nama karyawan : "))
    jabatan = str(input("masukan jabatan karyawan (manager/staff): ")).lower()
    gaji_pokok = int(input("masukan gaji pokok karyawan : "))

    if jabatan == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0

    pajak = 0.05 * gaji_pokok
    gaji_bersih = gaji_pokok - pajak + tunjangan

    pajak = int(pajak)
    tunjangan = int(tunjangan)
    gaji_bersih = int(gaji_bersih)
    
    print("nama karyawan : ", nama)
    print("jabatan karyawan : ", jabatan)
    print("gaji pokoknya adalah : Rp.",gaji_pokok)
    print("pajak pph 5% jadi : ",pajak)
    print("mendapatkan tunjangan sebesar : Rp",tunjangan)
    print("jadi gaji bersih yang di dapatkan : Rp.", gaji_bersih)
menghitung_gaji()