import math
bola_merah = 8
bola_biru = 6
diambil = 3

total_bola = bola_merah + bola_biru
kombinasi = math.comb(total_bola, diambil)

print(f"Jumlah Bola Marah: {bola_merah}")
print(f"Jumlah Bola Biru: {bola_biru}")
print(f"Total Bola: {total_bola} ")
print(f"Total Kombinasi: {kombinasi} ")
