print("Masukkan ukuran balok (dalam cm)")

# Input balok
panjang = float(input("Masukkan panjang:"))
lebar = float(input("Masukkan lebar:"))
tinggi = float(input("Masukkan tinggi:"))

# Menghitung balok
volume = panjang * lebar * tinggi
luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
print (f"jadi valume baloknya adalah", volume)
print (f"jadi luas permukaan baloknya adalah", luas_permukaan)