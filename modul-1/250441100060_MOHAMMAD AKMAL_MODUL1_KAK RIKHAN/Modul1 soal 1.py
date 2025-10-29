# Barang Belanja
Harga_buku_tulis = 5000
Jumlah_buku_tulis = 3
Harga_pensil = 4500
Jumlah_pensil = 2
Pajak_pembelian = 0.1

# Menghitung Total 
total =(Harga_buku_tulis * Jumlah_buku_tulis) + (Harga_pensil * Jumlah_pensil) 
total_harga = total * Pajak_pembelian
print("Total jumlah pajak",(total_harga))
print("Harga awal sebelum ditambah pajak ",(total))
print("jadi total harga setelah ditambahkan pajak",(total_harga + total))