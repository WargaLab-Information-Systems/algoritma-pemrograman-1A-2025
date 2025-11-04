def gaji(nama,jabatan,gajipokok):

    pajak = 0.05 * gajipokok

    if jabatan == "manager":
        tunjangan = 0.10 * gajipokok
    elif jabatan == "staf":
        tunjangan = 0.05 * gajipokok
    else:
        tunjangan = 0

    totalgajibersih = gajipokok + tunjangan - pajak

    print("nama karyawan: ",nama)
    print("jabatan: ",jabatan) 
    print("gaji pokok Rp: ", gajipokok)
    print("tunjangan Rp: ",tunjangan)
    print("pajak pph 5% Rp: ",pajak)
    print("gaji bersih Rp: ",totalgajibersih)

    return totalgajibersih

nama = input("masukan nama karyawan: ")
jabatan = input("masukan jabatanya: ").lower()
while True:
    try:
        gajipokok = float(input("masukkan gaji pokok: "))
        if gajipokok < 0:
            print("gaji tidak boleh negatif, coba lagi")
            continue
        break
    except ValueError:
        print("input tidak valid, coba lagi")

gaji(nama,jabatan,gajipokok)