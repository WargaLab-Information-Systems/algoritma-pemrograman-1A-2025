GAJI_POKOK = 100000
BONUS_MALAM = 50000

total_gaji = 0
total_lembur_jam = 0
total_bonus_malam = 0

for hari in range(1, 8):
    print(f"\nHari {hari}:")
    
    jam_lembur = -1
    while jam_lembur < 0:
        input_str = input("Masukkan jumlah jam lembur: ")
        if input_str.isdigit():
            jam_lembur = int(input_str)
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif. Coba lagi.")
                jam_lembur = -1
        else:
            print("Input harus berupa angka bulat non-negatif. Coba lagi.")
    
    if jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        bayaran_lembur = 0
        jam_lembur = 0
    elif jam_lembur == 8:
        bayaran_lembur = 300000
    elif jam_lembur == 6:
        bayaran_lembur = 200000
    elif jam_lembur == 4:
        bayaran_lembur = 100000
    elif 1 <= jam_lembur <= 3:
        bayaran_lembur = 25000 * jam_lembur
    else:
        bayaran_lembur = 0

    shift_malam = input("Apakah hari ini shift malam? (y/n): ")
    
    bonus_malam = BONUS_MALAM if shift_malam == 'y' else 0
    gaji_hari = GAJI_POKOK + bayaran_lembur + bonus_malam

    total_gaji += gaji_hari
    total_lembur_jam += jam_lembur
    total_bonus_malam += bonus_malam
    print(f"Gaji hari ini: Rp{gaji_hari:,}")

print("Total setelah 7 hari:")
print(f"Total jam lembur            : {total_lembur_jam} jam")
print(f"Total bonus shift malam     : Rp{total_bonus_malam:,}")
print(f"Total gaji seminggu         : Rp{total_gaji:,}")