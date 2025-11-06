bola_M = 8
bola_B = 6
total_bola = bola_M + bola_B
di_ambil = 3
kombinasi = total_bola * (total_bola - 1) * (total_bola -2) // (di_ambil * (di_ambil - 1) * (di_ambil - 2))
print("Kemungkinan Jumlah kombinasi Bola Yang Dapat ambil Adalah : ",kombinasi) 