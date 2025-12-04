gaji = 100000
jam = 0
malam = 0
total_gaji = 0


for i in range(1, 8):
    bonus = 0
    print("Hari ke-", i)
    while True:
        try :
            lembur = int(input("Masukkan jumlah jam lembur (0-8) : "))
            if lembur < 0:
                print("Input tidak boleh negatif.")
                continue
            elif lembur > 8:
                print("Lembur melebihi batas, tidak dihitung.")
                lembur = 0
            break
        except ValueError:
            print("Input harus berupa angka. Masukkan kembali jam lembur anda (0-8)")
    if lembur >= 0 and lembur <= 3:
        bonus = 25000 * lembur
    elif lembur == 4 or lembur == 5:
        bonus = 100000
    elif lembur == 6 or lembur == 7:
        bonus = 200000
    elif lembur == 8:
        bonus = 300000
    else:
        bonus = 0
    jam += lembur
    shift = input("Apakah shift malam? (y/n) : ").lower()
    while shift not in ["y", "n"]:
        shift = input("Input y untuk ya atau input n untuk tidak. silahkan masukkan kembali (y/n) : ").lower()
    if shift == "y":
        bonusshift = 50000
        malam += 50000
    else :
        bonusshift = 0
    print("Gaji hari ini: Rp ", gaji + bonus + bonusshift)
    print()
    
    total_gaji += gaji + bonus + bonusshift
    
print()
print("Total jam lembur :", jam)
print("Total bonus shift malam: Rp", malam)
print("Total gaji : Rp", total_gaji)