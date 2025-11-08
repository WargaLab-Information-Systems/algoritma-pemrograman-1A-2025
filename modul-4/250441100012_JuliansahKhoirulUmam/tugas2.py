print("="*10," Tugas 2 Modul 4 ","="*20)
t_gaji = 0
t_lembur = 0
t_bonus = 0
for hari in range (1,8):
    print(f"Hari Ke-{hari}")

    jam_lembur = -1 
    while jam_lembur < 0 :
        input_str = input("Masukkan Jam Lembur anda : ")
        if input_str.isdigit():
            jam_lembur = int(input_str)
            if jam_lembur <0 :
                print("Jam lembur Tidak Boleh Negatif. Cobalagi.")
                jam_lembur = -1
        else:
            print("Input Harus Berupa Angka Bulat Non-negatif.cobalagi")

    shift_malam = ""
    while shift_malam != "y" and shift_malam != "t":
        shift_malam = input("Apakah Anda Shift Malam...? (y/t) : ")
        if shift_malam != "y" and shift_malam != "t":
            print("masukkkan y atau t")
    
        
    if jam_lembur <= 3:
        lembur = 25000 * jam_lembur
    elif jam_lembur == 4:
        lembur = 100000
    elif jam_lembur == 6:
        lembur = 200000
    elif jam_lembur == 8:
        lembur = 300000
    elif jam_lembur > 8:
        print("Lembur Melebihi Batas, Tidak Di hitung.")
        lembur = 0
    else:
        lembur = 0

    gaji = 100000
    bonus_malam = 50000 if shift_malam.lower() == 'y' else 0

    t_harian = gaji + lembur + bonus_malam
    t_gaji += t_harian
    t_lembur += jam_lembur
    t_bonus += bonus_malam

print("\n---- Rekapan Gaji Mingguan ----")
print(f"Total Lembur :{t_lembur} Jam")
print(f"Total Bonus Shift Malam : Rp{t_bonus}")
print(f"Total Gaji 7 Hari : Rp{t_gaji}")