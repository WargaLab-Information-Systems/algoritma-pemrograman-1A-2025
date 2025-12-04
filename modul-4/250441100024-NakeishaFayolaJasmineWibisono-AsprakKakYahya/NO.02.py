total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"Hari ke-{hari}")
    while True:
        jam = int(input("Masukkan jam lembur: "))
        if jam < 0:
            print("Angka tidak boleh negatif")
        else:
            break
    shift_malam = input("Apakah shift malam? (ya/tidak): ").lower()
        
    gaji_pokok = 100000
    lembur = 0
        
    if jam <= 3 and jam >= 0:
        lembur = jam * 25000
    elif jam == 4:
        lembur = 100000
    elif jam == 8:
        lembur = 300000
    elif 4 < jam < 8:
        lembur = 200000
    elif lembur > 8:
        print("Lembur melebihi batas, maka tidak dihitung.")
    if lembur < 0:
        print ("Input tidakk boleh negatif")
        
    if shift_malam == "ya":
        bonus = 50000
    else:
        bonus = 0
        
    #total gajii
    gaji_harian = gaji_pokok + lembur + bonus 
    
    print(f"Gaji hari ini: Rp{gaji_harian}")
    
    total_gaji += gaji_harian
    total_lembur += lembur
    total_bonus += bonus
   
            
    
print("====== REKAP GAJI MINGGUAN ======")
print(f"Total lembur: Rp{total_lembur}")
print(f"Total bonus shift malam: Rp{total_bonus}")
print(f"Total gaji seminggu: Rp{total_gaji}")
    