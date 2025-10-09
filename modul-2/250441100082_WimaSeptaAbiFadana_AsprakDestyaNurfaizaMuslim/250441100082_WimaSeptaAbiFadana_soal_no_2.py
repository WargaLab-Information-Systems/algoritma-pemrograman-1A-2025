harga_tiket= 50000
usia= int(input("masukan usia anda :  "))
status= input("apakah anda seorang pelajar SMA (ya/tidak) : ")
hari= input("hari anda membeli tiket : ")

diskon= [0.0]

if usia < 12:
    diskon.append (0.50)
if status == "ya":
    diskon.append (0.30)
if hari == "selasa":
    diskon.append (0.20)


diskon= max(diskon)
total_harga= (harga_tiket * (1 - diskon))

print("harga tiket normalnya : Rp.", harga_tiket)
print("mendapatkan diskonnya : ", int(diskon * 100), "%")
print("jadi total yang harus di bayar : Rp.", int(total_harga))