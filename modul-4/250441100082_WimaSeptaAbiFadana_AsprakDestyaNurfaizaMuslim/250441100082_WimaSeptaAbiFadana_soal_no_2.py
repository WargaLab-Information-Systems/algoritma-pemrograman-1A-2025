total_gaji = 0
total_lembur = 0
total_bonus_shift = 0


for i in range(1,8):
    print("sekarang hari ke", i)

    while True:
        jam_lembur = input("berapa jam anda lembur : ")
        no = "0123456789"
        valid = True
        for i in jam_lembur:
            if i not in no:
                valid = False
                break
        if valid and jam_lembur != "":
            jam_lembur = int(jam_lembur)
            break
        else:
            print("input tidak valid masukan angka")

    while True:
        shift = input("apakah hari itu shift malam (y/n) : ").lower()
        if shift in ("y", "n"):
            break
        else:
            print("input tidak valid masukan (y/n)!")

    gaji_pokok = 100000

    if jam_lembur <= 3:
        bonus = jam_lembur * 25000
    if jam_lembur == 4:
        bonus = 100000
    if jam_lembur == 6:
        bonus = 200000
    if jam_lembur == 8:
        bonus = 300000
    if jam_lembur > 8:
        bonus = 0
        print("lembur meelebihi batas")
    bonus_shift = 50000 if shift == "y" else 0

    total_perhari = gaji_pokok + bonus + bonus_shift
    total_gaji += total_perhari
    total_lembur += jam_lembur
    total_bonus_shift += bonus_shift

print("jadi total jam lemburnya : ", total_lembur, "jam")
print("jadi total bonus shiftnya : Rp.", total_bonus_shift)
print("jadi total gaji nya dalam seminggu adalah : Rp.", total_gaji)