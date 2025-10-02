# Total belanja Halim beserta pajaknya

buku = 3 * 4500
pensil = 2 * 5000
total_barang = buku + pensil
pajak = 0.10 * total_barang
total_bayar = total_barang + pajak

print(f"Total belanja sebelum pajak: Rp {total_barang:,.2f}")
print(f"Pajak (10%): Rp {pajak:,.2f}")
print(f"Total yang harus dibayar Halim: Rp {total_bayar:,.2f}")