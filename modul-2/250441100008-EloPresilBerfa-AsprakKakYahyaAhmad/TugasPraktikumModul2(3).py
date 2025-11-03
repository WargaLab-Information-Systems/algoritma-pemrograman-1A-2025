print("="*50)
print("Nama : Elo Presil Berfa")
print("NIM : 250441100008")
print("="*50)

# Soal

# Sebuah mall menerapkan tarif parkir dengan ketentuan sebagai berikut :
# a. 2 jam pertama : Rp5.000
# b. Setiap jam berikutnya : Rp3.000
# c. Maksimal tarif parkir per hari : Rp20.000
# Kemudian mall ini juga memiliki aturan tambahan yaitu jika pengunjung adalah member VIP, biaya parkir langsung Rp0. Buatlah program python yang menerima input lama parkir (jam) dan status VIP, lalu hitung total biaya parkir.

# Jawaban
jam = int(input("Lama durasi parkir (jam): "))
status = input("Apakah Anda member VIP (ya/tidak): ").lower()

if status == "ya":
    tarif = 0
else:
    if jam == 0:
        tarif = 0
    elif jam > 0 and jam <= 2:
        tarif = 5000
    else:
        tarif = 5000 + (jam - 2) * 3000
if tarif > 20000:
    print("Peringatan: Tarif parkir melebihi batas maksimal harian sebesar Rp20.000")
else:
    print("Total tarif adalah: Rp", tarif)
    
print("="*50)











