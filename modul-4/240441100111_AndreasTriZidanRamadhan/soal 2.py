gaji = 100000
total_gaji = 0
lembur = 0
total_jam_lembur = 0
shift_malam = 0

for i in range (1,8):
    while True:
        print(f"Hari ke-{i}")
        jam_lembur = input("masukkan jumlah jam lembur karyawan: ")

        if jam_lembur.isdigit():
            jam_lembur = int(jam_lembur)
            if jam_lembur < 4 and jam_lembur > 0:
                lembur = jam_lembur * 25000
                total_jam_lembur += jam_lembur
            elif jam_lembur == 4 or jam_lembur == 5:
                lembur =  100000
                total_jam_lembur += jam_lembur
            elif jam_lembur == 6 or jam_lembur == 7:
                lembur =  200000
                total_jam_lembur += jam_lembur
            elif jam_lembur == 8:
                lembur =  300000
                total_jam_lembur += jam_lembur
            else:
                print("lembur melebihi batas, tidak dihitung")
            while True:    
                shift = input("Apakah lembur shift malam? (y/n): ").lower()
                if shift == 'y':
                    lembur += 50000
                    shift_malam += 50000
                    break
                elif shift == 'n':
                    break
                else:
                    print("input salah, tidak dihitung")
                    continue
        else:
            print("input salah, masukkan angka")
            continue
        break
    total_gaji = total_gaji + gaji + lembur
print(f"Total jam lembur karyawan dalam seminggu: {total_jam_lembur} jam")
print(f"Total bonus shift malam: Rp{shift_malam}")
print(f"Total gaji karyawan dalam seminggu: Rp{total_gaji}")
