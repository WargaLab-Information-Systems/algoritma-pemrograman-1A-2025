# Soal 1
# Hallim pergi ke sebuah toko alat tulis untuk membeli beberapa perlengkapan sekolah. Ia membeli 3 buah buku tulis dengan harga satuan Rp 5.000 dan 2 buah pensil dengan harga satuan Rp 4.500 selain itu, toko tersebut memberlakukan pajak pembelian sebesar 10% dari total harga barang. Lalu Hallim harus menghitung berapa uang yang harus ia bayar ke kasir setelah di tambahkan pajak. Buatlah program untuk menghitung total belanja setelah pajak ditetapkan!

# Jawaban Soal 1
harga_buku = 5000
harga_pensil = 4500
jumlah_buku = 3
jumlah_pensil = 2
pajak = 0.1

total_harga_buku = jumlah_buku * harga_buku
total_harga_pensil = jumlah_pensil * harga_pensil

total_sebelum_pajak = total_harga_buku + total_harga_pensil
harga_akhir = total_sebelum_pajak + (total_sebelum_pajak * pajak)

print("===========================================")
print("harga sebelum diskon adalah: ", total_sebelum_pajak)
print("pajak yang dikenakan adalah: ", pajak)
print("harga yang harus dibayar adalah: ", harga_akhir)
print("===========================================")