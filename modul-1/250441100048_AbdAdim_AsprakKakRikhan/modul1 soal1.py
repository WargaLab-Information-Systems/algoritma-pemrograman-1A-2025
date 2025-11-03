# Barang Belanja 
Harga_buku_tulis = 5000
Jumlah_buku_tulis = 3
Harga_pensil = 4500
Jumlah_pensil = 2
Pajak_pembelian = 0.10

# Penjumlahan
total =(Harga_buku_tulis * Jumlah_buku_tulis) + (Harga_pensil * Jumlah_pensil) 
total_harga = total * Pajak_pembelian
print(f"Total jumlah pajak ",int(total_harga))
print (f"Harga awal sebelum ditambahkan pajak ", int(total))
print (f"jadi total harga setelah ditambahkan pajak",int(total_harga + total))