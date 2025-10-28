total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"Hari ke-{hari}")

    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur (0-8): "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif")
                continue
            else:
                0 <= jam_lembur <= 8
                break
        except:
            print("Input tidak valid! Harus angka.")

    # if jam_lembur > 0:
    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
        if shift_malam in ['y', 'n']:
            break
        else:
            print("Input tidak valid! Ketik 'y' atau 'n'.")
    # else:
    #     shift_malam = 'n'

    gaji_pokok = 100000
    gaji_lembur = 0
    bonus_shift = 0

    if 0 <= jam_lembur <= 3:
        gaji_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        gaji_lembur = 100000
    elif jam_lembur == 6:
        gaji_lembur = 200000
    elif jam_lembur == 8:
        gaji_lembur = 300000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        gaji_lembur = 0

    if shift_malam == 'y':
        bonus_shift = 50000
        total_bonus += bonus_shift
        
    total_harian = gaji_pokok + gaji_lembur + bonus_shift
    total_gaji += total_harian
    total_lembur += jam_lembur

    print(f"Gaji hari ke-{hari}: Rp{total_harian:,}")

print("="*50)
print(f"Total jam lembur     : {total_lembur} jam")
print(f"Total bonus shift malam : Rp{total_bonus:,}")
print(f"Total gaji seminggu     : Rp{total_gaji:,}")
print("="*50)