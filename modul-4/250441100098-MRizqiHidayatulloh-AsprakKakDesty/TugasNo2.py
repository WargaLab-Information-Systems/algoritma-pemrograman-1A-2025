# Program menghitung total gaji mingguan Pak Wowo

total_gaji = 0
total_bonus_shift = 0

# Perulangan selama 7 hari kerja
for hari in range(1, 8):
    print(f"\nHari ke-{hari}")
    
    # Validasi input jumlah jam lembur
    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
                print("Jumlah jam lembur tidak boleh negatif!")
                continue
            break
        except:
            print("Input harus berupa angka!")
    
    # Input apakah shift malam
    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
        if shift_malam in ["y", "n"]:
            break
        else:
            print("Input tidak valid! Masukkan hanya 'y' untuk ya atau 'n' untuk tidak.")

    # Gaji pokok per hari
    gaji_pokok = 100_000
    
    # Hitung lembur
    if 1 <= jam_lembur <= 3:
        lembur = jam_lembur * 25_000
    elif jam_lembur == 4:
        lembur = 100_000
    elif jam_lembur == 6:
        lembur = 200_000
    elif jam_lembur == 8:
        lembur = 300_000
    elif jam_lembur > 8:
        lembur = 0
        print("Lembur melebihi batas, tidak dihitung.")
    else:
        lembur = 0
    
    # Tambahkan bonus shift malam
    bonus = 50_000 if shift_malam == "y" else 0
    total_bonus_shift += bonus
    
    # Hitung total gaji hari itu
    gaji_harian = gaji_pokok + lembur + bonus
    total_gaji = total_gaji + gaji_harian
    
    print(f"Gaji hari ke-{hari}: Rp{gaji_harian}")

# Setelah 7 hari
print("\n--- Rangkuman Mingguan ---")
print(f"Total bonus shift malam: Rp{total_bonus_shift}")
print(f"Total gaji seminggu: Rp{total_gaji}")

