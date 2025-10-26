# Program menghitung harga tiket bioskop

harga_normal = 50000

usia = int(input("Masukkan usia: "))
pelajar = input("Apakah pelajar SMA dengan kartu pelajar? (ya/tidak): ").lower()
hari = input("Hari apa sekarang?: ").lower()

diskon = 0

# Menentukan diskon terbesar
if usia < 12 : 
    diskon = 50
if pelajar == "ya" and diskon < 30:
    diskon = 30
if hari == "selasa" and diskon < 20:
    diskon = 20

# Menghitung total harga 
total = harga_normal - (harga_normal * diskon / 100)

print("\n=== HARGA TIKET BIOSKOP ===")
print(f"Harga normal : Rp{harga_normal:,}")
print(f"Diskon       : {diskon}%")
print(f"Total Bayar  : Rp{int(total):,}")