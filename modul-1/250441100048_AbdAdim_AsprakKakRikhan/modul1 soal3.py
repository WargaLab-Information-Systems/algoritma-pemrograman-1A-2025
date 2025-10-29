bola_merah = 8
bola_biru = 6
ambil = 3

total_bola = bola_merah + bola_biru
kombinasi=(total_bola*(total_bola -1)*(total_bola -2))//(ambil*(ambil -1)*(ambil -2))

print("jumlah total bola adalah:",total_bola)
print("jumlah bola yang di ambil:",ambil)
print("jumlah kemungkinan kombinasi bola yang di ambil adalah:",kombinasi)