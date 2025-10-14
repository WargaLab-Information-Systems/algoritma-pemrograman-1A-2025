lama_parkir = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah member VIP? (ya/tidak): ").lower()

if vip == "ya":
    total = 0
else:
    if lama_parkir <= 2:
        total = 5000
    else:
        total = 5000 + (lama_parkir - 2) * 3000
    

    if total > 20000:
        total = 20000

print("Total biaya parkir: Rp.", total)