usia = int(input("Masukkan usia Anda:  "))
status = input("Apakah anda Pelajar? (Ya/Tidak) ").lower()
hari = input("Masukkan hari anda menonton (Senin / Selasa / Rabu / Kamis / Jumat / Sabtu / Minggu): ").lower()
tiket = 50000

if usia <= 12 :
    if hari == "selasa" :
        tiket = tiket - (tiket * 0.50)
    else :
        tiket = tiket - (tiket * 0.50)
elif usia >= 13 :
    if status == "ya" :
        if hari == "selasa" :
            tiket = tiket - (tiket * 0.30)
        else :
            tiket = tiket - (tiket * 0.30)
    else :
        if hari == "selasa" :
            tiket = tiket - (tiket * 0.20)
        else :
            tiket = tiket
else :
    tiket = tiket
print("Harga tiket yang harus dibayar: Rp", int(tiket))