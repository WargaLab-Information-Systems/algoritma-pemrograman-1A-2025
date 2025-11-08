#Soal nomor 3
#jumlah bola merah dan bola biru 
merah = 8
biru =6
total = merah + biru

#jumlah bola yang diambil
ambil = 3

#hitung kombinasi
kombinasi = total * (total - 1) * (total - 2) // 6

print("jumlah kemungkinan kombinasi bola yang bisa diambil adalah:", kombinasi)