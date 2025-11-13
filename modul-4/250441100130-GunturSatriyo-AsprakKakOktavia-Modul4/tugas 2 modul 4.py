print("Gaji Mingguan Pak Wowo ")

total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"Hari ke-{hari}")

    while True:
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif!")
            break

    if 1 <= jam_lembur <= 3:
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
    else:
        gaji_lembur = 0

    while True:
        shift = input("Apakah hari ini shift malam? (y/n): ")
        if shift in ['y', 'n']:
            break
        else:
            print("Input tidak valid! Masukkan 'y' atau 'n'.")

    if shift == 'y':
        bonus = 50000
    else:
        bonus = 0

    gaji_harian = 100000 + gaji_lembur + bonus
    total_gaji += gaji_harian
    total_lembur += jam_lembur
    total_bonus += bonus

    print(f"Gaji hari ke-{hari}: Rp{gaji_harian:,}")


print("Rekap Gaji Mingguan")
print(f"Total jam lembur 1 minggu : {total_lembur} jam")
print(f"Total bonus shift malam          : Rp{total_bonus:,}")
print(f"Total gaji 1 minggu      : Rp{total_gaji:,}")
