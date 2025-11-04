print("="*50)
print("Nama : Elo Presil Berfa")
print("NIM : 250441100008")
print("="*50)

# Soal

# Dalam sebuah kotak terdapat 8 bola merah dan 6 bola biru. Seorang anak akan mengambil 3 bola sekaligus secara acak. Buatlah program Python untuk menghitung berapa banyak kemungkinan kombinasi bola yang dapat diambil!

# Jawaban
bola_merah = 8
bola_biru = 6
diambil = 3 
total_bola = bola_biru + bola_merah

kombinasi_bola = (total_bola * (total_bola - 1) * (total_bola - 2)) / (diambil * (diambil - 1) * (diambil - 2))
print("Banyaknya kemungkinan kombinasi bola adalah :",kombinasi_bola)