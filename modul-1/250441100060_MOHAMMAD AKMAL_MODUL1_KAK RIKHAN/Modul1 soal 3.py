# Data bola
Bola_merah = 8 
Bola_biru = 6
kombinasi_3_bola = 3

# Inputan
Bola_merah = float(input("Masukkan Bola merah:"))
Bola_biru = float(input("Masukkan Bola biru:"))
kombinasi_3_bola = float(input("Masukkan jumlah kombinasi bola:"))

# Menghitung kombinasi bola
Total_bola = (Bola_merah + Bola_biru)
print(f"total bola: {Total_bola} bola")
kombinasi_3_bola = (Total_bola * (Total_bola - 1) * (Total_bola - 2)) // 6
print(f"Jumlah kemungkinan kombinasi warna bola yang akan diambil adalah: {kombinasi_3_bola} warna")