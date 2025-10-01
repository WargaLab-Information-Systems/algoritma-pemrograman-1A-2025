jumlah_buku = 3 
jumlah_pensil = 2

harga_satuan_buku = 5000
harga_satuan_pensil = 4500

total_harga = (harga_satuan_buku * jumlah_buku) + (harga_satuan_pensil * jumlah_pensil)

pajak = 0.10 * total_harga

total_bayar = total_harga + pajak

print("total harga sebelum pajak",total_harga)
print("pajak 10%",pajak)
print("total yang harus di bayar",total_bayar)