total_gaji = 0
total_harian = 0
for hari in range(1, 8):
    while True:
        try:
            lembur = int(input(f"Jam lembur hari ke-{hari}: "))
            break
        except ValueError:
            print("Masukkan Angka!")
    while True:
        shift = input("Shift malam (y/n): ").lower()
        if shift in ["y","n"]:
            break
        else:
            print  ("Masukkan huruf Y atau N")
            
    gaji_pokok = 100000
    gaji_lembur= 0
    if lembur <= 3:
        gaji_lembur= lembur * 25000
    elif lembur == 4 or lembur == 5:
        bonus_lembur= 100000
        gaji_lembur += bonus_lembur
    elif lembur == 6 or lembur == 7:
        bonus_lembur = 200000
        gaji_lembur += bonus_lembur
    elif lembur == 8:
        bonus_lembur = 300000
        gaji_lembur += bonus_lembur
    elif lembur > 8 :
        print("Lembur melebihi batas ,  tidak dihitung")

    if shift == "y":
       bonus_shift = 50000
    else:
        bonus_shift= 0

    


    total_harian = gaji_pokok + gaji_lembur + bonus_shift
    total_gaji += total_harian

    print(f"Gaji hari ke-{hari}: Rp{total_harian:,}")
    print("====================================")
print(f"Total gaji seminggu: Rp{total_gaji:,}")
print("====================================")