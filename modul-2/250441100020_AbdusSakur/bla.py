# soal no.2
tiketNormal = 50000

usia = int(input("masukkan usia: "))
status = input("apakah pelajar SMA (ya/tidak): ")
hari = input("hari saat nonton: ")

if usia <= 12:
    diskon = 0.50
elif status == "ya":
    diskon = 0.30
elif hari == "selasa":
    diskon = 0.20
else:
    diskon = 0

hargaTiket = tiketNormal - (tiketNormal*diskon)

print(f" total harga tiket yang harus dibayar: Rp{hargaTiket:,.2f}")