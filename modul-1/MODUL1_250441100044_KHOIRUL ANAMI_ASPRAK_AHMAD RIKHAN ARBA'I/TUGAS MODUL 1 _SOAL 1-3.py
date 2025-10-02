# SOAL NO 1
# DATA PEMBELIAN
A = str("SOAL NO 1") 
print (A)
harga_buku = 5000
jumlah_buku = 3
harga_pensil = 4500
jumlah_pensil = 2 
pajak = 0.10

# MENGHITUNG TOTAL HARGA BARANG 
total_buku = harga_buku * jumlah_buku
total_pensil = harga_pensil * jumlah_pensil
total_awal = total_buku + total_pensil

# MENGHITUNG PAJAK
jumlah_pajak = total_awal * pajak

# MENGHITUNG TOTAL AKHIR UMTUK PEMBAYARAN

total_bayar = total_awal + jumlah_pajak

# MENAMPILKAN HASILNYA 

print (f"total harga buku  : Rp {total_buku:,}" )
print (f"total harga pensil : Rp {total_pensil:,}")
print (f"total keduanya dari pensil dan buku {total_awal:,}")
print (f"pajak (10%) Rp:  {jumlah_pajak:,} ")
print (f"total bayar Rp : {total_bayar:,}")

# SOAL NO 2
# MENGHITUNG VOLUME DAN LUAS PERMUKAAN BALOK

# INPUT DARI PENGGUNA
B = str("SOAL NO 2") 
print(B)
panjang = float (input("Silahkan masukkan panjang balok yang kamu inginkan: "))
lebar = float (input("Silahkan masukkan lebar balok yang kamu inginkan: "))
tinngi = float (input("Silahkan masukkan volume balok yang kamu inginkan: "))

# MENGHITUNG VOLUME

volume = panjang * lebar * tinngi

# MENGHITUNG LUAS PERMUKAAN BALOK
luas_permukaan = 2 *(panjang * lebar + panjang * tinngi + lebar * tinngi)

# MENAMPILKAN HASIL

print(f"Panjang : {panjang} cm")
print(f"Lebar : {lebar} cm")
print(f"Tinggi :{tinngi} cm")
print (f"Jadi volumenya adalah :{volume} cm³")
print (f"dan luas permukaannya adalah {luas_permukaan} cm²")

# SOAL NO 3
# MENGHITUNG JUMLAH KEMUNGKINAN UNTUK KOMBINASI PENGAMBILAN BOLA

C = str("SOAL NO 3") 
print (C) 
# JUMLAH BOLA
bola_merah = 8
bola_biru = 6
total_bola = bola_merah + bola_biru

#BANYAK BOLA YANG DIAMBIL
diambil = 3 
n = 14 * 13 * 12
r = 3 * 2 * 1

# MENGHITUNG KOMBINASI

kombinasi = n // r

# MENAMPILKAN HASIL 


print(f"Jumlah bola merah : {bola_merah}")
print(f"Jumlah bola biru : {bola_biru}")
print(f"Total bola adalah : {total_bola}")
print(f"Jadi banyak cara mengambil {diambil} bola sekaligus adalah: {kombinasi}")
