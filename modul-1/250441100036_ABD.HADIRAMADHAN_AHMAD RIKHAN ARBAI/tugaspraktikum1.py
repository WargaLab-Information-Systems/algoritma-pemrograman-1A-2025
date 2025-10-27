harga_buku = 5000
harga_pensil = 4500
jumlah_buku = 3
jumlah_pensil = 2

total_harga = (harga_buku * jumlah_buku) + (harga_pensil * jumlah_pensil)
pajak = 0.10 * total_harga
total_bayar = total_harga + pajak

print("Total harga sebelum pajak: Rp", total_harga)
print("Pajak (10%): Rp", pajak)
print("Total yang harus dibayar: Rp", total_bayar)