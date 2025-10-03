panjang = int(input("masukkan panjang balok (cm): "))
lebar = int(input("masukkan lebar balok (cm): "))
tinggi = int(input("masukkan tinggi balok (cm): "))

volume = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print(f"Volume balok: {volume} cm^3")
print(f"Luas permukaan balok: {luas_permukaan} cm^2")