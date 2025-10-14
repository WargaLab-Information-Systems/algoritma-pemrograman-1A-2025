#soal no 2
harga_tiket = 50000

usia = int(input("masukkan usia pengunjung bioskop:"))
if usia < 16:
    status_pelajar = "usia tersebut tidak termasuk usia anak sma"
    hari_nonton =input("masukkan hari nonton di bioskop: ")
else:
    status_pelajar = input("pelajar sma dengan kartu pelajar?(ya/tidak):")
    hari_nonton =input("masukkan hari nonton di bioskop: ")
diskon= 0

#mengecek diskon yang diterapkan 
if usia >=1  and usia <12 :
    if 50 > diskon:
        diskon=50
    
if status_pelajar == "ya" and usia >= 12 :
    if 30 > diskon :
        diskon =30

if hari_nonton == "selasa":
    if 20 > diskon:
        diskon= 20         
        
#menghitung harga diskon
harga_diskon = harga_tiket - (harga_tiket * diskon/100) 
#hasil 
if diskon == 0 :
    print("tidak dapat diskon")
else:
    print(f"Diskon: {diskon} %")
    print(f"Total yang harus dibayar:, Rp.{harga_diskon}")
