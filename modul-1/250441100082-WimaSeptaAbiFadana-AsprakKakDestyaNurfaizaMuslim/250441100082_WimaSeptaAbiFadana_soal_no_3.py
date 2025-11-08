import math
bola_merah= 8
bola_biru= 6
mengambil_bola= 3

total_bola= bola_biru + bola_merah
kombinasi= math.comb(total_bola, mengambil_bola)

print(f"jumlah bola merah : ", bola_merah)
print(f"jumlah bola biru : ", bola_biru)
print(f"total keseluruhan jumlah bola : ", total_bola)
print(f"bola yang di ambil : ", mengambil_bola)
print(f"Banyaknya kemungkinan kombinasi bola yang dapat diambil : ", kombinasi)