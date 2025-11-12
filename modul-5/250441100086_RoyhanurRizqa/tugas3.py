def perusahaan ():
    while True:
        nama=input("masukkan nama karyawan : ")
        jabatan=input("masukkan jabatan : ").lower()
        if jabatan not in ("manager", "staff"):
            print("jabatan harus berupa 'manager' atau ' staff'")
            continue
        gaji_pokok=int(input("masukkan gaji pokok :Rp"))
        if gaji_pokok <0:
            print("gaji pokok tidak boleh negatif")
            continue 
        return nama,jabatan,gaji_pokok

def perhitungan(x,y):    
    pajak=x*0.05
    gaji_pajak=x-pajak
 
    if y == "manager":
        gaji_tunjangan=x*0.1

    elif y == "staff":
        gaji_tunjangan=x*0.05

    gaji_bersih=gaji_pajak+gaji_tunjangan 
    return pajak,gaji_bersih,gaji_tunjangan,gaji_pajak

nama,jabatan,gaji_pokok=perusahaan() 
pajak,gaji_bersih,gaji_tunjangan,gaji_pajak=perhitungan(gaji_pokok,jabatan)

print("======== data gaji perusahaan =========")
print("Nama       : ",nama)
print("Jabatan    : ",jabatan)
print("gaji pokok : Rp",int(gaji_pokok))
print("pajak      : Rp",int(pajak))
print("tunjangan  : Rp",int(gaji_tunjangan)) 
print("gaji bersih: Rp",int(gaji_bersih)) 