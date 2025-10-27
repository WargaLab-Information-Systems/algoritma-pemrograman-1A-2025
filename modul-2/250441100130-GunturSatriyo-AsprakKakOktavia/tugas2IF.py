print("Nama : Guntur Satriyo")
print("NIM : 250441100130")
print("Tugas No 2 Praktikum")

harga_normal = 50000

usia = int(input("Masukkan usia: "))
status_pelajar = input("Apakah Anda pelajar SMA dengan kartu pelajar? (ya/tidak): ")
hari = input("Masukkan hari: ")

if usia < 12:
    diskon = 50
elif status_pelajar == "ya" :
    diskon = 30
elif hari == "selasa" :
    diskon = 20
else:
    diskon = 0

harga_bayar = harga_normal - (harga_normal * diskon / 100)

print("anda mendapatkan diskon", diskon, "%")
print("Harga tiket yang harus dibayar: Rp", int(harga_bayar))