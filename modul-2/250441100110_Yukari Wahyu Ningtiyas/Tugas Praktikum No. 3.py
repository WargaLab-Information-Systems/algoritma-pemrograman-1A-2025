# Tarif parkir mall

jam = int(input("Masukkan lama parkir (jam) : "))
vip = input("Apakah VIP (ya/tidak) ? ")

# Jika VIP maka gratis
if vip == "ya":
    biaya = 0
else:
    # Menghitung biaya normal
    if jam <= 2:
        biaya = 5000
    else:
        biaya = 5000 + (jam - 2) * 3000

    # Batas maksimal
    if biaya > 20000:
        biaya = 20000
 
print("Total biaya parkir : Rp", biaya)