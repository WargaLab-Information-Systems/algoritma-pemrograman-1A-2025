bola_merah = 8
bola_biru = 6
total_bola = bola_merah + bola_biru

ambil = 3

kombinasi = (total_bola * (total_bola - 1) * (total_bola - 2)) // (ambil * (ambil - 1) * (ambil - 2))

print("Jumlah kombinasi mengambil 3 bola dari", total_bola, "bola adalah:", kombinasi)
