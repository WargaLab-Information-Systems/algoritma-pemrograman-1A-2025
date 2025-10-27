total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}:")
    
    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif. Coba lagi.")
                continue
            break
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
    
    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
        if shift_malam in ['y', 'n']:
            break
        else:
            print("Input tidak valid! Ketik 'y' untuk ya atau 'n' untuk tidak.")
    
    gaji_harian = 100000
    
    if 1 <= jam_lembur <= 3:
        tambahan_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        tambahan_lembur = 100000
    elif jam_lembur == 6:
        tambahan_lembur = 200000
    elif jam_lembur == 8:
        tambahan_lembur = 300000
    elif jam_lembur > 8:
        tambahan_lembur = 0
        print("Lembur melebihi batas, tidak dihitung.")
    else:
        tambahan_lembur = 0
    
    bonus_shift = 50000 if shift_malam == 'y' else 0
    
    gaji_harian += tambahan_lembur + bonus_shift
    
    total_gaji += gaji_harian
    total_lembur += jam_lembur
    total_bonus += bonus_shift

print(f"Total jam lembur: {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus:,}")
print(f"Total gaji seminggu: Rp{total_gaji:,}")