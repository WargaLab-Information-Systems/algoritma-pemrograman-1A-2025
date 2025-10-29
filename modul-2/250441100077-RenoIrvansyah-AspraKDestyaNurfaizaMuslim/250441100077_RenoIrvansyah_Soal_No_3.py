parkir = int(input("Masukkan berapa jam parkir: "))
status = input("Apakah VIP (Ya/Tidak) ").lower()

if status == "ya":
    biaya = 0
    print("Anda adalah member VIP")
elif status == "tidak":
    if parkir <= 2:
        biaya = 5000
    else:
        biaya = 5000 + (parkir - 2) * 3000
        if biaya > 20000:
            biaya = 20000

print("Biaya parkir: Rp", biaya)