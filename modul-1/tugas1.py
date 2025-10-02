
#harga barang
harga_buku = 5000
harga_pensil = 4500

# jumlah 
jumlah_buku = 3
jumlah_pensil = 2

total_harga = (harga_buku * jumlah_buku) + (harga_pensil * jumlah_pensil)

# hitung pajak 10%
pajak = 10/100 * total_harga


total_bayar = total_harga + pajak
print("total harga buku:",harga_buku * jumlah_buku)
print("total harga pensil :", harga_pensil * jumlah_pensil)
print("total_harga sebelum pajak :",total_harga)
print("pajak (10%) : Rp", pajak)
print("total_harga setelah pajak yang harus di bayar oleh hallim adalah:", total_bayar)

