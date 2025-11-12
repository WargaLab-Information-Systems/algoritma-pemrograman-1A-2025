# Program Menghitung Tarif Parkir Mall

print("=== Program Hitung Biaya Parkir ===")

# Input
lama_parkir = int(input("Masukkan lama parkir (jam): "))
status_vip = input("Apakah Anda member VIP? (ya/tidak): ").lower()

# Jika member VIP, gratis
if status_vip == "ya":
    total_biaya = 0
else:
    # Tarif normal
    if lama_parkir <= 2:
        total_biaya = 5000
    else:
        total_biaya = 5000 + (lama_parkir - 2) * 3000
    
    # Batas maksimal per hari
    if total_biaya > 20000:
        total_biaya = 20000

# Output
print("\n=== Hasil Perhitungan ===")
print(f"Lama parkir: {lama_parkir} jam")
print(f"Status VIP: {status_vip}")
print(f"Total biaya parkir: Rp{total_biaya:}")
