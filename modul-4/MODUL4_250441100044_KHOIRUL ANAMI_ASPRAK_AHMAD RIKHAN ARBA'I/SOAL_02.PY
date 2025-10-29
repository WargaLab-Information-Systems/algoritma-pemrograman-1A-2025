# SOAL NO 2

X = str("SOAL NO 2")
print(X)

jumlah_hari = 7
bonus = 50000
gaji_pak_wowo = 100000
lembur = 0
total_gaji_seminngu = 0
total_lembur = 0
total_bonus_shif_malam = 0

for hari in range (1, jumlah_hari + 1):

    jam_lembur = int(input("Silahkan masukkan jumlah jam lembur anda disini ya😊: "))
    if jam_lembur < 0 :
        print("Mohon maaf jam lembur tidak boleh negative ya...😒")
        break
    
    elif jam_lembur == 0:
        lembur_sekarang = 0
    elif 1 <= jam_lembur <= 3 :
        lembur_sekarang = jam_lembur * 25000
    elif jam_lembur == 4:
        lembur_sekarang = 100000
    elif jam_lembur == 5:
        lembur_sekarang = 125000   
    elif jam_lembur == 6:
        lembur_sekarang = 200000
    elif jam_lembur == 7:
        lembur_sekarang = 175000
    elif jam_lembur == 8:
        lembur_sekarang = 300000
    elif jam_lembur > 8:
        print("Maaf lembur melebihi batas, kami tidak menghitungnya. ")
        break
    
    gaji_perhari = gaji_pak_wowo + lembur_sekarang 

    jumlah_bonus_shif = str(input("Apakah hari itu termasuk shif malam ? (IYA / TIDAK) "))
    if jumlah_bonus_shif .lower() != "iya" and jumlah_bonus_shif .lower()  != "tidak":
        print ("Input tidak valid, harus (iya / tidak)😒")
        break

    if jumlah_bonus_shif .lower() == "iya":
        print("Selamat anda mendapatkan bonus tambahan sebesar Rp : 50.000 😁 ")
        gaji_perhari += bonus
        total_bonus_shif_malam += bonus

    print (f"Jadi untuk hari sekarang pak wowo mendapatkan gaji sebesar {gaji_perhari}")

    total_gaji_seminngu += gaji_perhari
    total_lembur += jam_lembur

print (f"Jadi total jam lembur yang di peroleh pak wowo {total_lembur} jam ")
print (f"Total bonus shif malam sebanyak {total_bonus_shif_malam} bonus")
print (f"Sehinnga total gaji pak wowo selama 1 minggu adalah {total_gaji_seminngu}")
print ("SELAMAT PAK WOWO...😁😁😁")

