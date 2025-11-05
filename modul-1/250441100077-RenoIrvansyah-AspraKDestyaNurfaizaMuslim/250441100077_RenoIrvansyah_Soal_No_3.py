bola_merah = 8
bola_biru = 6
total_bola = bola_merah + bola_biru
bola_diambil = 3
kombinasi = total_bola * (total_bola - 1) * (total_bola - 2) // (bola_diambil * (bola_diambil - 1) * (bola_diambil - 2))

print("Jumlah kemungkinan kombinasi bola yang dapat diambil:", kombinasi)