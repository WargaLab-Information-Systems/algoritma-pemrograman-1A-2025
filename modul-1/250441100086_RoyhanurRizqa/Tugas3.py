print("Dalam sebuah kotak terdapat 8 bola merah dan 6 bola biru. Seorang anak akan mengambil 3 bola sekaligus secara acak.")
print("berapa banyak kemungkinan kombinasi bola yang dapat diambil!")

import math

total_bola=8+6
bola_yang_diambil=3
kombinasi=math.comb(total_bola,bola_yang_diambil)

print("jadi kemungkinan kombinasi bola yang diambil adalah :",kombinasi)