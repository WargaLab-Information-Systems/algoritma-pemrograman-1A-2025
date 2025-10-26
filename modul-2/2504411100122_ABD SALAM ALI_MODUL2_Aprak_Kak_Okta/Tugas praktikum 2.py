usia = int(input("masukkan usia: "))
pelajar = input("apakah peajar SMA dengan kartu? (ya/tidak):")
hari = input("hari nonton: ")
harga = 50000
# cari diskon terbesar
diskon = 0
if usia < 12:
   diskon = 50
elif pelajar == "ya":
   diskon = 30
elif hari == "selasa":
   diskon = 20
# hitung total
total = harga - (harga * diskon/100)
print("total yang harus dibayar: RP", total)