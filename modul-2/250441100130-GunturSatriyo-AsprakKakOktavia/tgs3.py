print("TUGAS 3 GUNTUR SATRIYO")

parkir = int(input("Berapa Jam Anda Parkir Di Mall : "))

status = input(("Apakah Ada Member VIP (ya/tidak)"))

if status == "ya" :
    tarif = 0
else:
    if parkir <= 2: 
        tarif = 5000
    else: 
        tarif = 5000 + (parkir - 2) * 3000
    if tarif > 20000: 
        tarif = 20000

print(f"Total Biaya Parkir Rp. {tarif:,}")