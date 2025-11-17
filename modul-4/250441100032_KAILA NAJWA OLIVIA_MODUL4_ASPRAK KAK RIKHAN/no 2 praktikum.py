# Program untuk menghitung gaji mingguan Pak Wowo
# Inisialisasi variabel total
total_gaji = 0
total_jam_lembur = 0
total_bonus_shift_malam = 0
# Loop untuk 7 hari
for hari in range(1, 8):
    print(f"\nHari {hari}:")
    # Input jam lembur dengan validasi
    while True:
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif. Coba lagi.")
                continue
            elif jam_lembur > 8:
                print("Lembur melebihi batas, tidak dihitung.")
                jam_lembur = 0 
            break
            print("input tidak valid,angka masukkan angka")
    # Input shift malam dengan validasi
    while True:
        shift_malam = input("Apakah shift malam? (y/n): ")
        if shift_malam in ('y', 'n'):
            break
        else:
            print("Input harus 'y' atau 'n'. Coba lagi.")
    
    # Hitung tambahan lembur
    if jam_lembur in (1, 2, 3):
        tambahan_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        tambahan_lembur = 100000
    elif jam_lembur == 6:
        tambahan_lembur = 200000
    elif jam_lembur == 8:
        tambahan_lembur = 300000
    else:
        tambahan_lembur = 0  # Jika >8 atau 0
    
    # Hitung bonus shift malam
    bonus = 50000 if shift_malam == 'y'  else 0
        
    # Hitung gaji hari ini
    gaji_hari = 100000 + tambahan_lembur + bonus
    
    # Akumulasi total
    total_gaji += gaji_hari
    total_jam_lembur += jam_lembur       
    total_bonus_shift_malam += bonus
    
    # Tampilkan gaji hari ini 
    print(f"Gaji hari {hari}: Rp{gaji_hari:,}")
# Tampilkan hasil akhir
print("Hasil Akhir:")
print(f"Total jam lembur: {total_jam_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus_shift_malam:,}")
print(f"Total gaji seminggu: Rp{total_gaji:,}")