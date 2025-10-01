print("="*50)
print("Nama : M RIZQI HIDAYATULLOH")
print("NIM : 250441100098")
print("="*50)

# Soal

# Dalam sebuah kotak terdapat 8 bola merah dan 6 bola biru. Seorang anak akan mengambil 3 bola sekaligus secara acak. Buatlah program Python untuk menghitung berapa banyak kemungkinan kombinasi bola yang dapat diambil!

# Jawaban
import math
# Bola
merah = 8
biru = 6
diambil = 3

total_bola = merah + biru
kombinasi = math.comb(total_bola, diambil)

print(f"Jumlah Bola Merah: {merah}")
print(f"Jumlah Bola Biru: {biru}")
print(f"Total Bola: {total_bola}")
print(f"Bola yang Diambil: {diambil}")
print(f"Total Kombinasi: {kombinasi}")