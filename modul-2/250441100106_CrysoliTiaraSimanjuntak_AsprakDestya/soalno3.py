# Program Menghitung Biaya Parkir

jam = int(input("Masukkan lama parkir (jam):"))
vip = input("Apakah Anda member VIP? (ya/tidak):").lower()

# Jika VIP, gratis
if vip == "ya":
    total = 0
else:
    if jam <= 2:
        total = 5000
    else:
        total = 5000 + (jam - 2) * 3000
        if total > 20000:
            total = 20000

print("\n=== BIAYA PARKIR ===")
print(f"Lama Parkir : {jam} jam")
print(f"Status VIP  : {vip} ")
print(f"Total bayar : Rp{total}:,") 