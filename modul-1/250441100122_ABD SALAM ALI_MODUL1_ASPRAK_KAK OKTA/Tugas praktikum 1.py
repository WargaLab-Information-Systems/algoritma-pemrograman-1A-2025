#data pembelian 
jumlah_buku = 3
jumlah_pensil = 2
harga_satuan_buku = 5000
harga_satuan_pensil = 4500
pajak = 0.1

total_harga_buku = jumlah_buku * harga_satuan_buku
total_harga_pensil = jumlah_pensil * harga_satuan_pensil

total_sebelum_pajak = total_harga_buku + total_harga_pensil
harga_akhir = total_sebelum_pajak + (total_sebelum_pajak * pajak)

print("=================================")
print("Rincian Pembayaran Hallim")
print("harga sebelum pajak:", total_sebelum_pajak)
print("pajak yang dikenakan:", pajak)
print("total yang harus dibayar:", harga_akhir)
print("=================================")