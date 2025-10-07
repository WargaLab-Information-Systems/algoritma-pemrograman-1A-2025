# Soal 2 - Harga Tiket Bioskop

harga_normal = 50000

usia = int(input("Masukkan usia: "))
pelajar = input("Apakah pelajar SMA yang memiliki kartu pelajar? (ya/tidak): ")
hari = input("Masukkan hari: ")

diskon = 0

if usia < 12:
    diskon = 50
if pelajar == "ya":
    diskon = max(diskon, 30)
if hari == "selasa":
    diskon = max(diskon, 20)

harga_bayar = harga_normal - (harga_normal * diskon / 100)

print("Diskon:", diskon, "%")
print("Harga yang harus dibayar: Rp", int(harga_bayar))
