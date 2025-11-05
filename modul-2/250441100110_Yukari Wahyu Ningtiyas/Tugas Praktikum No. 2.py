# Harga normal tiket
harga = 50000

usia = int(input("Masukkan usia: "))
pelajar = input("Apakah pelajar SMA (ya/tidak)? ")
hari = input("Masukkan hari: ")

# Menentukan diskon
if usia < 12:
    diskon = 50
elif pelajar == "ya":
    diskon = 30
elif hari == "selasa":
    diskon = 20
else:
    diskon = 0

# Menghitung harga akhir
harga_akhir = harga - (harga * diskon / 100)

print("Harga tiket yang harus dibayar: Rp", int(harga_akhir))