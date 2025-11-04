# SOAL NO 3
X = str("SOAL NO 3")
print(X)
# TARIF PARKIR MALL

# MASUKKAN DATA
jam = int(input("Silahkan masukkan lama parkir anda (jam): "))
vip = input("Apakah anda merupakan pengunjung dengan member vip (ya/tidak)? ")

# PENYELEKSIAN KONDISI
if vip == "ya":
    biaya = 0
else:
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
        else:
            biaya = sisa_jam  * 3000 + 20000 
            
# HASIL
print(f"Jadi total biaya parkir kamu sebesar: Rp{biaya}")


