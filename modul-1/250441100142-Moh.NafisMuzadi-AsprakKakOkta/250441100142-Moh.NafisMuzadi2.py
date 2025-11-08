panjang = float(input ("masukkan panjang balok : "))
lebar = float(input ("masukkan lebar balok : "))
tinggi = float(input ("masukkan tinggi balok : "))

volume = panjang * lebar * tinggi

luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi )

print("volume balok adalah :", volume, "cm")
print("luas balok adalah :", luas, "cm")
