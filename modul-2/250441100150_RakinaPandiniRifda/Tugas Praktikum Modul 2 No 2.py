# Keterangan harga beserta diskonnya
harga_nominal = 50000
diskon = 0.0

# Input data
try:
    usia = int(input("Usia: "))
    pelajar = input("Pelajar SMA dengan kartu pelajar(ya/tidak): ")
    hari = input("Hari nonton selasa(ya/tidak): ")
except:
    print("Input usia tidak valid.")
    exit()

# Penentuan diskon terbesar (maksimal)
if usia < 12:
    diskon = max(diskon, 0.50)
if pelajar == 'ya':
    diskon = max(diskon, 0.30)
if hari == 'selasa':
    diskon = max(diskon, 0.20)

# Output
harga_akhir = harga_nominal - (harga_nominal * diskon)
print(f"\nDiskon diterapkan: {int(diskon * 100)}%")
print(f"Total harga tiket: Rp{harga_akhir:,.0f}")