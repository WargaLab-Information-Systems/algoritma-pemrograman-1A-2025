print("="*10,"TUGAS 3 TARIF PARKIR MALL","="*10)

#inputan pengguna
parkir = int(input("Berapa Jam Anda Parkir Di Mall : "))
status = input(("Apakah Ada Member VIP (y/t)")).lower()

#menghitung tarif
if status == "y" :
    tarif = 0
else :
    if parkir <= 2 : # 2 jam pertama Rp 5,000
        tarif = 5000
    else : # Jika Lebih, 2 Jam + sisa Jam Berikutnya Dan Bertarif Mulai 3000 
        tarif = 5000 + (parkir - 2) * 3000
        if tarif > 20000 : # maksimal Tarif Perhari Rp 20,000
            tarif = 20000
# Outputan
print(f"Total Biaya Parkir : Rp.{tarif:,}")   
