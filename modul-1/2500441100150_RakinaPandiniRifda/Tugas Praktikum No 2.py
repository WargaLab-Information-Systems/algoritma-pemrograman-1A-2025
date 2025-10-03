# Menghitung Volume dan Luas Permukaan Balok

# Input
p = float(input("Masukkan panjang (cm): "))
l = float(input("Masukkan lebar (cm): "))
t = float(input("Masukkan tinggi (cm): "))

# Rumus untuk memproses
volume = p * l * t
luas = 2 * (p*l + p*t + l*t)

# Output
print("--- Hasil ---")
print(f"Volume: {volume:.2f} cm³")
print(f"Luas Permukaan: {luas:.2f} cm²")