total_gaji = 0
total_jam_lembur = 0
total_bonus_malam = 0

for n in range(1, 8):
    print(f"Hari {n}:")

    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
                print("Jam lembur tidak valid. Silakan coba lagi.")
                continue
            break
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

    total_jam_lembur += jam_lembur
    
    if jam_lembur == 0:
        gaji_lembur = 0
    elif 1 <= jam_lembur <= 3:
        gaji_lembur = 25000
    elif 4 <= jam_lembur <= 5:
        gaji_lembur = 100000
    elif 6 <= jam_lembur <= 7:
        gaji_lembur = 200000
    elif jam_lembur == 8:
        gaji_lembur = 300000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        gaji_lembur = 0
    
    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
        if shift_malam in ("y", "n"):
            break
        else:
            print("Input harus (y/n). Silakan coba lagi.")
    
    bonus = 50000 if shift_malam == "y" else 0
    total_bonus_malam += bonus
    
    gaji_hari = 100000 + gaji_lembur + bonus
    total_gaji += gaji_hari

print(f"Total jam lembur: {total_jam_lembur}")
print(f"Total bonus shift malam: Rp{total_bonus_malam}")
print(f"Total gaji seminggu: Rp{total_gaji}")