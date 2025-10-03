# Soal 3
# Dalam sebuah kotak terdapat 8 bola merah dan 6 bola biru. Seorang anak akan mengambil 3 bola sekaligus secara acak. Buatlah program Python untuk menghitung berapa banyak kemungkinan kombinasi bola yang dapat diambil.

# Jawaban Soal 3
import math
bola_merah = 8
bola_biru = 6
kasus = 3

jumlah_total_bola = bola_merah + bola_biru
kombinasi_bola = math.comb(jumlah_total_bola, kasus)

print("===========================================")
print(f"Jumlah bola merah: {bola_merah}")
print(f"Jumlah bola biru: {bola_biru}")
print(f"Total bola: {jumlah_total_bola}")
print(f"Jumlah bola yang diambil: {kasus}")
print(f"Total kombinasi: {kombinasi_bola}")
print("===========================================")