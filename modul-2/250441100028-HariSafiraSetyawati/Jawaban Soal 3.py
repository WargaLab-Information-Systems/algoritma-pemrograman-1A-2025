jam = int(input("Masukkan lama durasi parkir (dalam jam): "))
status = input("Apakah anda member VIP? (ya/tidak): ")

if status == "ya":
    biaya = 0
else:
    if jam <= 2:
        biaya = 5000
    elif jam <= 7:
        biaya = 5000 + (jam - 2) * 3000

if biaya > 20000:
    print("Biaya parkir melebihi batas maksimal RP20.000")

print("Biaya parkir yang harus dibayar: Rp", biaya)