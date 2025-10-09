jam = float(input("masukkan berapa jam anda parkir "))
status = input("apakah anda merupakan VIP (iya/tidak)")
if status == "iya":
    tarif = 0
    print("tarif anda adalah ", tarif)
else:
    hari = jam // 24
    sisa = jam % 24
    total_hari = hari*20000
    if hari > 0:
        tarif = sisa*3000 + total_hari
        print("biaya anda setelah parkir ", hari, " hari dan", sisa, "jam ", tarif)
    elif sisa > 0:
        tarif = 0
        if sisa <= 2:
            tarif = 5000+total_hari
            print("biaya anda setelah parkir ", hari, " hari dan", sisa, "jam ", tarif)
        elif sisa > 2:
            tarif = (sisa-2)*3000+5000+total_hari
            print("biaya anda setelah parkir ", hari, " hari dan", tarif)


