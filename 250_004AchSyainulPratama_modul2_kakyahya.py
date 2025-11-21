
usia = int(input("Masukkan usia: "))
pelajar = input("Apakah pelajar SMA dengan kartu? (ya/tidak): ").lower()
hari = input("Hari nonton: ").upper()

harga = 50000


# Cari diskon terbesar
diskon = 0
if usia < 12:
    diskon = 0.50
elif pelajar == "ya":
    diskon = 0.30
elif hari == "SELASA":
    diskon = 0.20

# Hitung total
total = harga *(1 - diskon)

print("Total yang harus dibayar: Rp", total)

# Input data vip 
jam = int(input("Lama parkir (jam): "))
vip = input("Apakah VIP? (ya/tidak): ")

# Jika VIP, gratis
if vip == "ya":
    total = 0
else:
    if jam == 0:
        total = 0
    elif jam <= 2:
        total = 5000
    else:
        total = 5000 + (jam - 2) * 3000

    # Batas maksimal 20 ribu
    if total > 20000:
        total = 20000

print("Total biaya parkir: Rp", total)
