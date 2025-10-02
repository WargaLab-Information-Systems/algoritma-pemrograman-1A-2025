print("Masukkan ukuran balok (dalam cm):")

# Input dari pengguna
panjang = float(input("Panjang: "))
lebar = float(input("Lebar: "))
tinggi = float(input("Tinggi: "))

# Hitung volume
volume = panjang * lebar * tinggi

# Hitung luas permukaan
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Output hasil
print("\nHasil Perhitungan:")
print(f"Volume balok: {volume} cm³")
print(f"Luas permukaan balok: {luas_permukaan} cm²")
 