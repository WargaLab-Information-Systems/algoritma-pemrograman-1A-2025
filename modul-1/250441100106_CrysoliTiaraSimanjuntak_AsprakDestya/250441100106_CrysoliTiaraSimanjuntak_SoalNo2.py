# Input panjang, lebar, tinggi
panjang = float(input("Masukkan panjang balok (cm): "))
lebar = float(input("Masukkan lebar balok (cm): "))
tinggi = float(input("Masukkan tinggi balok (cm): "))

# Menghitung volume
volume = panjang * lebar * tinggi

# Menghitung luas permukaan
luas_permukaan = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)

# Hasil
print("Volume balok = ", volume, "cm³")
print("Luas permukaan balok = ", luas_permukaan, "cm²")