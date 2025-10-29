print("program menghitung volume dan luas permukaan sebuah balok")
panjang=int(input("masukkan nilai panjang :")) #di isi 10
lebar=int(input("masukkan nilai lebar :")) #di isi 6
tinggi=int(input("masukkan nilai tinggi :")) # di  isi 4
volume=panjang*lebar*tinggi
luas_permukaan=2*((panjang*lebar)+(panjang*tinggi)+(lebar*tinggi))
print("volume baloknya adalah :",volume)
print("luas permukaan baloknya adalah :",luas_permukaan)