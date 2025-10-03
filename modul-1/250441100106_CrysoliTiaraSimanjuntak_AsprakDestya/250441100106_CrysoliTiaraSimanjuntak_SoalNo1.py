# Harga barang
harga_buku = 5000
harga_pensil = 4500

# Jumlah barang
jumlah_buku = 3
jumlah_pensil = 2

# Menghitung total harga
total_harga = (jumlah_buku * harga_buku) + (jumlah_pensil * harga_pensil)

# Menghitung pajak 10%
pajak = total_harga * 0.10

# Menghitung total bayar
total_bayar = total_harga + pajak

# Hasil
print("Total harga :", total_harga)
print("Pajak 10% :", pajak)
print("Total bayar :", total_bayar)