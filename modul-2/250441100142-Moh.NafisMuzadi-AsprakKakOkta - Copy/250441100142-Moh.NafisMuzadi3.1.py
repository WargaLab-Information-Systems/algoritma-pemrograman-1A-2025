lama = float(input("Masukkan lama anda parkir disini (dalam jam): "))
status = input("Apakah anda member VIP? (Ya/Tidak) ").lower()
tarif = 5000
tarif_per_jam = 3000

if lama <= 2 :
    if status == "ya" :
        tarif = 0
    tarif = tarif
elif lama > 2 :
    tarif = tarif + ((lama - 2) * tarif_per_jam)
    if status == "ya" :
        tarif = 0
if tarif > 20000 :
    tarif = 20000
else :
    tarif = tarif
print("Tarif parkir yang harus dibayar: Rp.", int(tarif))