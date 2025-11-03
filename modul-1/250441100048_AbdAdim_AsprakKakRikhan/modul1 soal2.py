#soal2
panjang = 10
lebar = 6
tinggi = 4

print("Masukkan ukuran balok (dalam cm)")

panjang = float(input("Masukkan panjang:"))
lebar = float(input("Masukkan lebar:"))
tinggi = float(input("Masukkan tinggi:"))

volume = panjang * lebar * tinggi
luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
print (f"jadi valume baloknya adalah", volume)
print (f"jadi luas permukaan baloknya adalah", luas_permukaan)