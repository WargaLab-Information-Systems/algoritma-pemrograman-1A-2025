#nomer2
panjang = int(input("masukkan panjang balok (cm):"))
lebar = int(input("masukkan lebar balok (cm):"))
tinggi = int(input("masukkan tinggi balok (cm):"))
#menghitung
volume = panjang * lebar * tinggi
luas_permukaan_balok = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)

#outputnya
print("=== HASILNYA ===")
print("volume balok :", volume,)
print("luas permukaan balok :",luas_permukaan_balok)