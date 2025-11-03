usia = int(input("Masukkan usia: "))
pelajar = input("Apakah pelajar SMA? (ya/tidak): ").lower()
hari = input("Masukkan hari: ").lower()

harga_normal = 50000
diskon = 0

if usia < 12:
    diskon = 0.5  # 50%
elif pelajar == "ya":
    diskon = 0.3  # 30%
elif hari == "selasa":
    diskon =  0.2  # 20%
else:
    diskon = 0 

harga_bayar = harga_normal - (harga_normal * diskon)
print("Harga tiket yang harus dibayar: Rp.", int(harga_bayar))
