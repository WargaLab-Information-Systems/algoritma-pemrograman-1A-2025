print("=== Program Gaji Mingguan Pak Wowo ===")

total_gaji = 0          
total_lembur = 0        
total_bonus = 0         

# Loop selama 7 hari
for hari in range(1, 8):
    print(f"\nHari ke-{hari}")

    # Validasi input agar tidak error
    while True:
        try:
            lembur = int(input("Masukkan jumlah jam lembur: "))
            if lembur < 0:
                print("Jam lembur tidak boleh negatif. Coba lagi.")
                continue
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka.")

    # Input shift malam dengan validasi
    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
        if shift_malam in ["y", "n"]:
            break
        else:
            print("Input harus 'y' untuk ya atau 'n' untuk tidak.")

    # Gaji pokok per hari
    gaji_pokok = 100000

    # Hitung tambahan lembur berdasarkan aturan
    if lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        tambahan = 0
        lembur = 0
    elif lembur == 7 or 8:
        tambahan = 300000
    elif lembur == 5 or 6:
        tambahan = 200000
    elif lembur == 4:
        tambahan = 100000
    elif 1 <= lembur <= 3:
        tambahan = lembur * 25000
    else:
        tambahan = 0

    # Bonus shift malam
    if shift_malam == "y":
        bonus = 50000
    else:
        bonus = 0

    # Akumulasi total mingguan
    total_gaji += gaji_pokok + tambahan + bonus
    total_lembur += lembur
    total_bonus += bonus

# Tampilkan hasil akhir
print("\n=== REKAPITULASI GAJI MINGGUAN ===")
print(f"Total jam lembur : {total_lembur} jam")
print(f"Total bonus shift malam : Rp {total_bonus}")
print(f"Total gaji seminggu : Rp {total_gaji}")
