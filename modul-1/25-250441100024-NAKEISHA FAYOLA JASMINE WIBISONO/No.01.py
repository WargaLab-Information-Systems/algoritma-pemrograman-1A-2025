# #nomor 1
# harga_buku = 5000
# harga_pensil = 4500
# jumlah_buku = 3
# jumlah_pensil = 2

# total_belanja = jumlah_buku * harga_buku + jumlah_pensil * harga_pensil
# jumlah_pajak = 0.1
# pajak = total_belanja * jumlah_pajak
# total_bayar = total_belanja + pajak

# #outputnya
# print ("total_belanja: Rp", total_belanja)
# print ("pajak (10%): Rp", jumlah_pajak)
# print ("total yang harus dibayar: Rp", total_bayar)

#nomer2
panjang = int(input("masukkan panjang balok (cm):"))
lebar = int(input("masukkan lebar balok (cm):"))
tinggi = int(input("masukkan tinggi balok (cm):"))
#menghitung
volume = panjang * lebar * tinggi
luas_permukaan_balok = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)

#outputnya
print("=== HASILNYA ===")
print("volume balok :", volume,)
print("luas permukaan balok :",luas_permukaan_balok)

# #nomer 3
# import math
# merah = 8
# biru = 6 
# ambil = 3

# total = math.comb(merah+biru, ambil)


# rincian = {
#     "3 merah": math.comb(merah, 3) *math.comb(biru, 0),
#     "2 merah = 1 biru": math.comb (merah, 2) * math.comb(biru, 1),
#     "1 merah + 2 biru": math.comb(merah, 1) * math.comb(biru, 2),
#     "3 biru": math.comb(merah, 0) * math.comb(biru, 3),
# }

# print("total kombinasi:", total)
# for k, v in rincian.items():
#     print(f"{k}: {v} cara")