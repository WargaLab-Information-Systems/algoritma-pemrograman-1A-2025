panjang = int(input("Masukkan panjang: "))
lebar = int(input("Masukkan lebar: "))
tinggi = int(input("Masukkan tinggi: "))

volume = panjang * lebar * tinggi
print("Volume balok adalah:", volume)

luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
print("Luas permukaan balok adalah:", luas_permukaan)