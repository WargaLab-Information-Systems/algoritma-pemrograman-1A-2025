# Menghitung gaji mingguan Pak Wowo
print("=== Program Hitung Gaji Mingguan Pak Wowo ===")

total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}:")
    
    # Input jumlah jam lembur (harus angka dan tidak negatif)
    while True:
        jam_input = input("Masukkan jumlah jam lembur: ")
        try:
            jam_lembur = float(jam_input)
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif.")
                continue
            jam_lembur = int(jam_lembur)
            break
        except:
            print("Input tidak valid. Masukkan angka yang benar.")
    
    # Input shift malam (y/n)
    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
        if shift_malam in ["y", "n"]:
            break
        else:
            print("Input hanya boleh 'y' atau 'n'.")
    
    # Gaji harian
    gaji_harian = 100000

    if jam_lembur == 0:
        tambahan_lembur = 0
    elif 1 <= jam_lembur <= 3:
        tambahan_lembur = jam_lembur * 25000
    elif 4 <= jam_lembur <= 8:
        # Setiap jam di atas 3 dihitung +50.000 dari jam sebelumnya
        tambahan_lembur = 100000 + (jam_lembur - 4) * 50000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        tambahan_lembur = 0
    else:
        tambahan_lembur = 0

    # Bonus shift malam
    if shift_malam == "y":
        bonus = 50000
    else:
        bonus = 0

    # Total per hari
    total_harian = gaji_harian + tambahan_lembur + bonus

    total_gaji += total_harian
    total_lembur += jam_lembur
    total_bonus += bonus

# Hasil rekap mingguan
print("\n=== Rekap Mingguan Pak Wowo ===")
print(f"Total jam lembur: {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus:,}")
print(f"Total gaji seminggu: Rp{total_gaji:,}")