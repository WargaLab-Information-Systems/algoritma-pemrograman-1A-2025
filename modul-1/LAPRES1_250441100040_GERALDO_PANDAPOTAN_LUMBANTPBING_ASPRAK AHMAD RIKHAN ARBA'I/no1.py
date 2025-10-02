# Barang Belanjaan Hallim
harga_buku = 5000
jumlah_buku = 3
harga_pensil = 4500
jumlah_pensil = 2

# Pajak Toko
pajak = 0.10

# Hitung Total Belanjaan sebelum pajak
total_belanja = harga_buku*jumlah_buku + harga_pensil*jumlah_pensil

# Menghitung Pajak
pajak = total_belanja * pajak

# Uang Yang Harus Dibayar Setelah Di Tambahkan Pajak
total_bayar = total_belanja + pajak

# Menampilkan Hasil
print("Total Harga Sebelum Pajak",total_belanja) 
print("pajak (10%)",pajak)
print("Uang Yang Harus Hallim Bayar Setelah Diskon Adalah :",total_bayar)

