total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")
    jam = int(input("Masukkan jam lembur (0 jika tidak ada): "))
    shift = input("Shift malam? (y/n): ").strip().lower()

    # gaji pokok harian
    gaji_pokok = 100000

    # hitung lembur (maksimal 8 jam)
    if 1  <= jam <= 3:
        lembur = jam * 25000
    elif jam == 4:
        lembur = 100000
    elif jam == 6:
        lembur = 200000
    elif jam == 8:
        lembur = 300000
    else:
        lembur = 0
        if jam > 8:
            print("Lembur melebihi batas, tidak dihitung")

    # bonus shift malam
    bonus_malam = 50000 if shift == "y" else 0

    # total akumulasi mingguan
    total_gaji += gaji_pokok + lembur + bonus_malam
    total_lembur += lembur
    total_bonus += bonus_malam

print("\n=== HASIL AKHIR ===")
print(f"Total lembur minggu ini   : Rp{total_lembur}")
print(f"Total bonus shift malam   : Rp{total_bonus}")
print(f"Total gaji minggu ini     : Rp{total_gaji}")