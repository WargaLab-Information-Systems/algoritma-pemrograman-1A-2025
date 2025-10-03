panjang = float(input("masukkan panjang "))
lebar = float(input("masukkan lebar "))
tinggi = float(input("masukkan tinggi "))

luas = 2*(panjang*lebar + panjang*tinggi + lebar*tinggi)
volume = panjang*lebar*tinggi

print(f"luas balok {luas}")
print(f"volume balok {volume}")