# Program Harga Tiket Bioskop

print("=== Program Hitung Harga Tiket Bioskop ===")

# Input data
usia = int(input("Masukkan usia: "))
pelajar = input("Apakah Anda pelajar SMA? (ya/tidak): ").lower()
hari = input("Masukkan hari: ").lower()

# Harga normal
harga_tiket = 50000

# Cek diskon yang berlaku
diskon = 0

if usia < 12:
    diskon = 50
elif pelajar == "ya":
    diskon = 30
elif hari == "selasa":
    diskon = 20

# Hitung harga akhir
harga_diskon = harga_tiket - (harga_tiket * diskon / 100)

# Output hasil
print("\n=== Hasil Perhitungan ===")
print(f"Usia: {usia} tahun")
print(f"Pelajar SMA: {pelajar}")
print(f"Hari: {hari.capitalize()}")
print(f"Diskon: {diskon}%")
print(f"Harga yang harus dibayar: Rp{harga_diskon:}")
