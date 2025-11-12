total_gaji = 0
total_jam_lembur = 0
total_bonus_shift = 0

for hari in range(1, 8):
    while True:
        try:
            lembur = int(input(f"Masukkan jam lembur hari ke-{hari}: "))
            if lembur < 0:
                print("Jam lembur tidak boleh negatif.")
                continue
            shift = input("Apakah shift malam? (y/n): ").lower()
            if shift not in ['y', 'n']:
                print("Input shift tidak valid, gunakan y atau n.")
                continue
        except :
            print("Input tidak valid, masukkan angka untuk jam lembur.")
            continue
        break

    gaji_harian = 100000  
    bonus_lembur = 0

    if 1 <= lembur <= 3:
        bonus_lembur = lembur * 25000
    elif lembur == 4 or 5:
        bonus_lembur = 100000
    elif lembur == 6 or 7:
        bonus_lembur = 200000
    elif lembur == 8:
        bonus_lembur = 300000
    elif lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")

    if shift == "y":
        bonus_shift = 50000
        total_bonus_shift += bonus_shift
    else:
        bonus_shift = 0
    
    gaji_harian = gaji_harian + bonus_lembur + bonus_shift
    total_gaji += gaji_harian
    total_jam_lembur += lembur

print(f"Total jam lembur: {total_jam_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus_shift:,}")
print(f"Total gaji seminggu: Rp{total_gaji:,}")