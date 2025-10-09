# Program Tarif Parkir Mall

# Input Jam dan Status
jam = int(input("Masukkan lama parkir (jam): "))
status = input("Apakah Anda member VIP? (ya/tidak): ")

# Proses
if status == "ya":
    biaya = 0
else:
    if jam <= 2:
        biaya = 5000
    else:
        biaya = 5000 + (jam - 2) * 3000

    # Batasi biaya maksimal
    if biaya > 20000:
        biaya = 20000

# Output
print("Total biaya parkir: Rp", biaya)