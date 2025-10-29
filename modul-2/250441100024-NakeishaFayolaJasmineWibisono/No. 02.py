harga_normal = 50000

usia = int(input("Masukkan usia: "))
pelajar = input("Apakah pelajar SMA dengan kartu (ya/tidak)? ").lower()
hari = input("Masukkan hari :")

diskon = 0
#cek diskon
if usia < 12:
    diskon = 50
elif pelajar == "ya":
        diskon = 30
elif hari == "Selasa":
        diskon = 20
else:
    diskon = 0
    
#harga akhir
harga_bayar = harga_normal - (harga_normal * diskon / 100)

print ("diskon =", diskon, "%")
print ("harga tiket yang harus di bayar: Rp", int(harga_bayar))  


    





