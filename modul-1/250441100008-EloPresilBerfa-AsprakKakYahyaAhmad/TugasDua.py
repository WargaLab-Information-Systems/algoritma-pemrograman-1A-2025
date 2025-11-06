print("="*50)
print("Nama : Elo Presil Berfa")
print("NIM : 250441100008")
print("="*50)

# Soal

# Seorang siswa sedang belajar tentang bangun ruang. Ia diminta menghitung volume dan luas permukaan sebuah balok dengan ukuran: Panjang = 10cm Lebar = 6 cm Tinggi = 4 cm, Buatlah program untuk membantu siswa tersebut menyelesaikan masalah tersebut! program tersebut bisa menerima input dari panjang, lebar, dan tinggi!

# Jawaban
panjang = int(input(" Input Panjang : "))
lebar = int(input(" Input Lebar : "))
tinggi = int(input(" Input Tinggi : "))

volume_balok = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print(" Volume balok tersebut adalah : ",volume_balok,"Cm Kubik")
print(" Luas permukaan balok tersebut adalah : ",luas_permukaan,"Cm Persegi")