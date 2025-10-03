# Soal 2
# Seorang siswa sedang belajar tentang bangun ruang. Ia diminta menghitung volume dan luas permukaan sebuah balok dengan ukuran:
# Panjang = 10 cm
# Lebar = 6 cm
# Tinggi = 4 cm
#Buatlah program untuk membantu siswa tersebut menyelesaikan masalah tersebut! program tersebut bisa menerima input dari panjang, lebar, dan tinggi!

# Jawaban Soal 2
panjang = int(input("Masukkan panjang : "))
lebar = int(input("Masukkan lebar : "))
tinggi = int(input("Masukkan tinggi : "))

volume = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print("===========================================")
print("Volume balok adalah : ", volume)
print("Luas permukaan balok adalah : ", luas_permukaan) 
print("===========================================")