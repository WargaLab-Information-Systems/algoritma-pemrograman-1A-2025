print ("nama : ach syainul pratama")
print ("NIM : 250441100004")

# Soal 1
buku = 3 * 5000
pensil = 2 * 4500
total = buku + pensil

diskon = total * 0.1
setelah_diskon = total - diskon

pajak = setelah_diskon * 0.1
total_bayar = setelah_diskon + pajak

print("Total sebelum diskon:", total)
print("Diskon:", diskon)
print("Setelah diskon:", setelah_diskon)
print("Pajak:", pajak)
print("Total bayar:", total_bayar)



# Fungsi untuk menghitung volume balok
panjang = int(input("Masukkan panjang: "))
lebar = int(input("Masukkan panjang: "))
tinggi = int(input("Masukkan panjang: "))

volume = panjang * lebar * tinggi
luas = 2*((panjang * lebar)+ (panjang*tinggi) + (lebar * tinggi))
print ("jadi volume dari balok tersebut adalah ", volume)
print ("jadi luas permukaan balok tersebut adalah", luas)



bola_merah = 8
bola_biru = 6
total_bola = bola_merah + bola_biru

# rumus kombinasi = n!/r!(n-r)1

rumus = (14*13*12)/(3*2*1)

print (" jadi jumlah kemungkinan kombinasi bola yang dapat diambil adalah" ,rumus)
