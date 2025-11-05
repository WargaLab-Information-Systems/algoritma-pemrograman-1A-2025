print("="*25," TUGAS Praktikum NO 2 ", "="*25)
 # Inputan Pengguna
usia = int(input("Masukan Usia Anda : "))
status = input(("Status Anda Pelajar SMA (y,t) ")).lower()
hari = input(("Apakah Anda Menonton Di Hari Selasa (y/t) : ")).lower()

# Menghitung Diskon
tiket = 50000
diskon = 0
if usia < 12 :
    diskon = 0.50
elif usia >= 12 or usia <= 50:
    if status == "y" :
        diskon = 0.30
    else :
        if hari == "y" :
            diskon = 0.20
        else :
            diskon = 0
else :
     if hari == "y" :
         diskon = 0.20
     else :
            diskon = 0

total = tiket - (tiket * diskon) # Rumus Diskon Adalah Harga Di kali 
#Outputan
print("/n ---- Rincian Pembayaran ----")
print(f"Harga Normal Tiket Adalah     : Rp{ tiket:,}")
print(f"Diskon Yang Di Dapat Adalah  :{diskon * 100}%")
print(f"Total Pembayaran Yang Harus Di Bayar Rp.{int(total):,}")


