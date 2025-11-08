# Soal 2: Volume dan luas permukaan balok
p = float(input("Masukkan panjang balok: "))
l = float(input("Masukkan lebar balok: "))
t = float(input("Masukkan tinggi balok: "))

volume = p * l * t
luas_permukaan = 2 * (p*l + p*t + l*t)

print("Volume balok =", volume, "cm^3")
print("Luas permukaan balok =", luas_permukaan, "cm^2")

