# no2
#Panjang = 10 cm
#Lebar = 6 cm
#Tinggi = 4 cm

#data balok
panjang = float(input("Masukkan panjang balok (cm): "))
lebar = float(input("Masukkan lebar balok (cm): "))
tinggi = float(input("Masukkan tinggi balok (cm): "))

#menghitung volume 
volume = panjang * lebar * tinggi

#menghitung luas permukaan 
luas_permukaan = (panjang * lebar + panjang * tinggi + lebar * tinggi)

print("Hasil Perhitungan Balok")
print(f"Panjang: {panjang} cm")
print(f"Lebar: {lebar} cm")
print(f"Tinggi: {tinggi}")
print(f"volume balok: {volume} cm")
print(f"luas permukaan balok: {luas_permukaan} cm")