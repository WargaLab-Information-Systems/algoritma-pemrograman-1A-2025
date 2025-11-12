# soal no 2

total_gaji = 0
total_lembur = 0
total_bonus = 0 

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")
    jam = int(input("Masukkan jumlah jam lembur: "))
    shift = input("Apakah shift malam? (y/n): ")

    gaji = 100000
    lembur = 0 

    if jam <= 3:
        lembur = jam * 25000
    elif jam == 4:
        lembur = 100000
    elif jam == 6:
        lembur = 200000
    elif jam == 8:
        lembur = 300000
    elif jam > 8:
        print("Lembur melebihi batas, tidak dihitung. ")

    if shift == "y" :
        bonus = 50000
    else:
        bonus = 0

    total_harian = gaji + lembur + bonus 
    print(f"Gaji hari ke-{hari}: Rp{total_harian:,}")
    
    total_gaji += total_harian
    total_lembur += lembur
    total_bonus += bonus

print("\n=== RINCIAN GAJI MINGGUAN ===")
print(f"Total lembur: Rp{total_lembur:,}")
print(f"Total bonus shift malam: Rp{total_bonus:,}")
print(f"Total gaji selama 7 hari: Rp{total_gaji:,}")