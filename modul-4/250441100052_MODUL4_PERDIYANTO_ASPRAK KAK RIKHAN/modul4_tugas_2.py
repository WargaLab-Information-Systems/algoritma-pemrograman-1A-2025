lama_kerja = 7
gaji_pokok = 100000
total_lembur = 0
total_bonus = 0
total = 0

for i in range(1, lama_kerja + 1):
    while True:
        try:
            lembur = float(input("masukan jumlah jam lembur "))
            total_lembur += lembur
            total += 100000
            break
        except ValueError:
            print("input tidak valid, lebur dianggap 0 jam")
            lembur = 0
    
    while True:
        hari = input("apakah masuk sift malam ? (y/n) ")

        if hari.lower() == "y":
            bonus = 50000
            total_bonus += bonus
            break
        elif hari.lower() == "n":
            break
        else:
            print("harus y atau n")
     
    if lembur > 0 and lembur < 4:
        perlembur = lembur * 25000
        print(f"bonus lembur hari ke - {i} = {perlembur}")
        total += perlembur

    elif lembur > 3 and lembur < 6:
        sisa = lembur - 4
        perlembur = (sisa * 25000) + 100000
        print(f"bonus lembur hari ke - {i} = {perlembur}")
        total += perlembur

    elif lembur > 5 and lembur < 8:
        sisa = lembur - 6
        perlembur = (sisa * 25000) + 200000
        print(f"bonus lembur hari ke - {i} = {perlembur}")
        total += perlembur
    
    elif lembur == 8:
        perlembur = 300000
        print(f"bonus lembur hari ke - {i} = {perlembur}")
        total += perlembur
    
    elif lembur > 8:
        print("lembur melebihi batas, tidak dihitung")
    
    elif lembur == 0:
        print("lembur 0, tidak dapat bonus")
    else:
        print("lembur tidak valid, harus lebih dari 0")

total = total + total_bonus
print("="*100)
print(f"\n total jam lembur           : {total_lembur} jam")
print(f"\n total bonus sift malam     : {total_bonus}")
print(f"\n total gaji selama seminggu : {total}")
print("="*100)