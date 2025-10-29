 # Program Soal 2 - Gaji Mingguan Pak Wowo

total_gaji = 0
total_lembur = 0
total_bonus = 0
total_jam = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")
    
    jam = int(input("  Masukkan jam lembur: "))
    shift = input("  Apakah shift malam (y/n)? ")

    # gaji pokok
    gaji_harian = 100_000

    # hitung lembur
    if jam >=1 and jam <=3:
        lembur = jam * 25_000
    elif jam == 4:
        lembur = 100_000
    elif jam == 6:
        lembur = 200_000
    elif jam == 8:
        lembur = 300_000
    elif jam > 8:
        lembur = 0
        print(" Lembur melebihi batas, tidak dihitung.")
    else:
        lembur = jam * 25_000  # jika jam 5 atau 7 (logis)

    # bonus shift malam
    if shift == 'y':
        bonus = 50_000
    else:
        bonus = 0

    total = gaji_harian + lembur + bonus
    print(f"  Total hari ke-{hari}: Rp{total:,}")

    # akumulasi total mingguan
    total_gaji += total
    total_lembur += lembur
    total_bonus += bonus
    total_jam += jam

print("\n--- RANGKUMAN GAJI MINGGUAN ---")
print(f"Total jam lembur = {total_jam} jam")
print(f"Total uang lembur = Rp{total_lembur:,}")
print(f"Total bonus shift malam = Rp{total_bonus:,}")
print(f"Total gaji mingguan = Rp{total_gaji:,}")

