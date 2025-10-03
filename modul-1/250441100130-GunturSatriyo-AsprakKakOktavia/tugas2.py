print("Nama : Guntur Satriyo")
print("NIM : 250441100130")
print("Tugas No 2 Praktikum")

#PENYELESAIAN SOAL NO 2

panjang = int (input(" Input Panjang : "))
lebar = int (input(" Input Lebar : "))
tinggi = int (input(" Input Tinggi : "))

volume = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print(" Jadi, Volume balok tersebut adalah : ",volume,"cm³")
print(" Jadi, luas permukaan balok tersebut adalah : ",luas_permukaan,"cm²")