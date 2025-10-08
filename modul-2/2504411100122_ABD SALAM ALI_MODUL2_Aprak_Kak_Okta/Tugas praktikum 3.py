# Program Menghitung Biaya Parkir di Mall
# Input lama parkir (dalam jam)
jam = int(input("Masukkan lama parkir (jam): "))
# Input status VIP
vip = input("Apakah Anda member VIP? (ya/tidak): ").lower()
# Jika pengunjung VIP, biaya parkir = 0
if vip == "ya":
    biaya = 0
else:
    if jam <= 2:
        biaya = 5000
    else:
        biaya = 5000 + (jam - 2) * 3000

    # Batas maksimal tarif per hari
    if biaya > 20000:
        biaya = 20000
# Output hasil
print("Total biaya parkir: Rp", biaya)