#Nomor 1 : Barang Belanjaan hallim 
harga_buku = 5000
jumlah_buku = 3
harga_pensil = 4500
jumlah_pensil = 2

#Pajak
pajak = 10/100

#Hitung Total Belanjaan 
total_buku = harga_buku*jumlah_buku
total_pensil = harga_pensil*jumlah_pensil
total_belanjaan = total_buku + total_pensil
#Uang Yang Harus Dibayar Setelah Pajak 
subtotal = total_belanjaan * pajak + total_belanjaan

#Menampilkan Hasil  
print("Uang Yang Harus Hallim Bayar Setelah Pajak Adalah:", subtotal)
