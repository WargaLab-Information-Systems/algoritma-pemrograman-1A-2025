import math

bola_merah = 8
bola_biru = 6
diambil = 3
total = bola_merah + bola_biru
kombinasi = math.comb(total, 3)

print("Jumlah kemungkinan kombinasi bola:", kombinasi)