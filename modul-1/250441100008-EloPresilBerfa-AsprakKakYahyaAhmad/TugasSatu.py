print("="*50)
print("Nama : Elo Presil Berfa")
print("NIM : 250441100008")
print("="*50)

#Soal
#Hallim pergi ke sebuah toko alat tulis untuk membeli beberapa perlengkapan sekolah. Ia membeli 3 buah buku tulis dengan harga satuan Rp 5.000 dan 2 buah pensil dengan harga satuan Rp 4.500 selain itu, toko tersebut memberlakukan pajak pembelian sebesar 10% dari total harga barang. Lalu Hallim harus menghitung berapa uang yang harus ia bayar ke kasir setelah di tambahkan pajak. Buatlah program untuk menghitung total belanja setelah pajak ditetapkan!

#Jawaban
buku = 5000
pensil = 4500
pajak = 0.1
total_harga = (3 * buku) + (2 * pensil) 
pajak_pembelian = total_harga * pajak
total_belanja = total_harga + pajak_pembelian

print("Total harga barang : Rp ",total_harga)
print("Total pajak : Rp ",pajak_pembelian)
print("Jadi, Hallim harus membayar sebesar Rp.",total_belanja)