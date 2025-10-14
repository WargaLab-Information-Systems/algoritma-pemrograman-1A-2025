#input variabel
jam = int(input("masukkan lama parkir (dalam jam): "))
vip = input("apakah mamber VIP? ")

#biaya jika
if vip =="ya":
    biaya = 0
else :
    if jam <= 24:
        if jam <= 2:
            biaya = 5000 
        else:
            biaya = 5000 + (jam - 2) * 3000
            if biaya > 20000:
                biaya = 20000
    else:
        hari_penuh = jam // 24
        sisa_jam = jam % 24
        biaya = hari_penuh * 20000

        if sisa_jam == 0:
            pass
        elif sisa_jam <= 12 :
            biaya = sisa_jam * 3000 + 20000
        else :
            sisa_jam * 3000 + 20000

#print hasil
print(f"jadi total biaya parkir sebesar : Rp {biaya}")    