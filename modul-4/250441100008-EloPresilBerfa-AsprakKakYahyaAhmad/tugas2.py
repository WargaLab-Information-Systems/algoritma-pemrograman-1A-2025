total_gaji = 0
total_lembur = 0
total_bonus_malam = 0

for hari in range(1, 8):
    print(f"Hari ke-{hari}")

    while True:
        jam = input("Masukkan jam lembur (0-8): ")
    
        valid = True
        for c in jam:
            if c < '0' or c > '9':
                valid = False
        
        if not valid or jam == "":
            print("Input tidak valid! Masukkan angka.")
            continue

        jam = int(jam)

        if jam > 8:
            print("Lembur melebihi batas, tidak dihitung.")
            jam = 0
            break
        else:
            break
        
    if jam >= 1 and jam <= 3:
        bonus_lembur = 25000 * jam
    elif jam == 4:
        bonus_lembur = 100000
    elif jam == 6:
        bonus_lembur = 200000
    elif jam == 8:
        bonus_lembur = 300000
    else:
        bonus_lembur = 0

    total_lembur += jam
    
    while True:
        malam = input("Apakah shift malam? (y/n): ").lower()
        if malam != "y" and malam != "n":
            print("Input hanya y atau n!")
        else:
            break

    bonus_malam = 50000 if malam == "y" else 0
    if malam == "y":
        total_bonus_malam += 50000

    gaji_harian = 100000 + bonus_lembur + bonus_malam
    total_gaji += gaji_harian

print("Total jam lembur:", total_lembur, "jam")
print("Total bonus shift malam: Rp", total_bonus_malam)
print("Total gaji seminggu: Rp", total_gaji)