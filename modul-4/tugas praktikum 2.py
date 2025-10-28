# Program Perhitungan Gaji Mingguan Pak Wowo
total_gaji = 0
total_lembur = 0
total_bonus_shift = 0

for hari in range(1, 8):  # 7 hari
    print(f"\nHari ke-{hari}")
    
    # Validasi input jam lembur
    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif. Coba lagi.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat.")
    
    # Validasi input shift malam
    while True:
        shift = input("Apakah shift malam? (y/n): ").lower()
        if shift in ['y', 'n']:
            break
        else:
            print("Input tidak valid. Masukkan 'y' atau 'n'.")
    
    # Gaji pokok harian
    gaji_harian = 100000
    
    # Hitung lembur
    if 1 <= jam_lembur <= 3:
        gaji_harian += jam_lembur * 25000
        total_lembur += jam_lembur
    elif jam_lembur == 4:
        gaji_harian += 100000
        total_lembur += jam_lembur
    elif jam_lembur == 5:
        gaji_harian += 125000
        total_lembur += jam_lembur
    elif jam_lembur == 6:
        gaji_harian += 200000
        total_lembur += jam_lembur
    elif jam_lembur == 7:
        gaji_harian += 225000
        total_lembur += jam_lembur
    elif jam_lembur == 8:
        gaji_harian += 300000
        total_lembur += jam_lembur
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
    # jika jam_lembur == 0, tidak ada tambahan

    # Bonus shift malam
    if shift == 'y':
        gaji_harian += 50000
        total_bonus_shift += 50000
    # Tambahkan ke total gaji
    total_gaji += gaji_harian
# Hasil akhir
print("\n=== Rekap Mingguan Pak Wowo ===")
print(f"Total jam lembur       : {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus_shift:,}")
print(f"Total gaji seminggu    : Rp{total_gaji:,}")