#no.3
#input variabel
jam = int(input("Masukkan lama parkir: "))
vip = input("apakah member VIP?: ")  

#biaya jika
if vip == "ya":
    biaya = 0
else:
    if jam <= 2:
        biaya = 5000
    else:
        biaya = 5000 + (jam - 2) * 3000

    #Batas biaya maksimal 20000
    if biaya > 20000:
        biaya = 20000

#outputnya
print ("Total biaya parkir: Rp", biaya)