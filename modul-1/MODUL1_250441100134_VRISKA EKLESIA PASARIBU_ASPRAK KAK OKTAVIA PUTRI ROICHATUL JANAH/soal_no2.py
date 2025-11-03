#Menghitung volume dan luas permukaan balok
#Program ini menerima input dari pengguna untuk Panjang, lebar, dan tinggi

panjang= float(input("masukkan panjang balok (cm): "))
lebar = float(input("masukkan lebar balok (cm): "))
tinggi = float(input("masukkan tinggi balo (cm): "))  

#Mengihiung Volume 
volume = panjang*lebar*tinggi

#menghitung luas permukaan 
luas_permukaan = 2* (panjang*lebar + panjang*tinggi + lebar*tinggi)

#hasil
print("Volume balok =", volume ,"cm³")
print("Luas permukan balok =", luas_permukaan, "cm²")