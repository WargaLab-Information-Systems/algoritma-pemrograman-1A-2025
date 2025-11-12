#MENGHITUNG HARGA
Beras =int(input("Masukan harga beras? "))
Gula = int(input("Masukan harga gula? "))
Minyak = int(input("Masukan harga gula? "))

while (Beras,Gula,Minyak):
    break
if Beras >= 100000 :
    diskon = 0.15
    print ("Mendapatkan diskon")
    
Pelanggan_yang_memiliki_member_card = 'Pelanggan_yang_memiliki_member_card mendapatkan diskon 5%'
Total_belanja =int(input('mendapat tambahan diskon 5% dari total akhir.' ))

if Total_belanja >= 100000 :
    diskon = 0.15
    print ("Mendapatkan diskon 10%")
elif Total_belanja >= 200000 :
    diskon = 0.10
    print ("Mendapatkan diskon 20%")
elif Pelanggan_yang_memiliki_member_card == "Memiliki member card":
    diskon = 0.5
    print("mendapat tambahan diskon 5% dari total akhir. ")
else: 
    print("Tidak mendapatkan diskon")

