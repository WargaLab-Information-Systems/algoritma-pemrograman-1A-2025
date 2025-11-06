print("="*50)
print("Nama : Elo Presil Berfa")
print("NIM : 250441100008")
print("="*50)

# Soal

#Sebuah bioskop memiliki aturan harga tiket:

#Kategori Harga/Diskon
#Tiket Normal Rp.50.000
#anak-anak < 12 tahun Diskon 50%
#pelajar SMA dengan kartu pelajar Diskon 30%
#penonton hari Selasa(promo)Diskon 20%.

#Jika ada lebih dari satu kondisi diskon yang berlaku, gunakan diskon terbesar. Buatlah program python yang dimana program meminta input usia, status pelajar (ya/tidak), dan hari, lalu cetak harga tiket yang harus dibayar.

# Jawaban

tiket = 50000
usia = int(input("Input Usia : "))
status_pelajar = input("Status Pelajar (ya/tidak) : ").lower()
kartu = input("Apakah punya kartu pelajar (ya/tidak) : ").lower()
hari = input("Input Hari : ").lower()

if usia < 12:
    diskon = 0.5
elif status_pelajar == "ya" and kartu == "ya":
        diskon = 0.3
elif hari == "selasa":
    diskon = 0.2
else:
    diskon = 0.0

persenan = int(diskon * 100)
total = tiket * (1 - diskon)

print("Anda Mendapatkan Diskon sebesar",persenan,"%")
print("Harga Tiket Anda Sebesar : Rp ",total)

print("="*50)
