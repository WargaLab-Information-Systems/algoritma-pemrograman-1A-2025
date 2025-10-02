 # jumlah bola 
bola_merah = 8
bola_biru   = 6

# total semua bola 
total_bola = bola_merah + bola_biru

# jumlah bola yang di ambil
ambil = 3 

# rumus kombinasi 
kombinasi = ( total_bola *( total_bola - 1 ) * (total_bola - 2)) // (ambil * (ambil - 1) * (ambil - 2))

# atas = 14 * 13 *12 = 2184
# bawah 3 * 2 *1    = 6

#tampilkan hasil
print("jumlah total bola adalah :", total_bola )
print("jumlah bola yang di ambil:", ambil)
print("jumlah kemungkinan kombinasi bola yang di ambil adalah :", kombinasi)

  