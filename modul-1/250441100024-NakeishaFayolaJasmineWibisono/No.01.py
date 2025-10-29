#nomor 1
harga_buku = 5000
harga_pensil = 4500
jumlah_buku = 3
jumlah_pensil = 2

total_belanja = jumlah_buku * harga_buku + jumlah_pensil * harga_pensil
jumlah_pajak = 0.1
pajak = total_belanja * jumlah_pajak
total_bayar = total_belanja + pajak

#outputnya
print ("total_belanja: Rp", total_belanja)
print ("pajak (10%): Rp", jumlah_pajak)
print ("total yang harus dibayar: Rp", total_bayar)

