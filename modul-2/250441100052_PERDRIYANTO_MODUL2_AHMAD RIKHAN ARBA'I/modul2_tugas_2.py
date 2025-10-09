#mendeklarsikan variabel
tiket_normal = 50000
diskon = 0
umur = int(input("masukkan umur anda "))
sma = input("apakah kamu pelajar SMA ? IYA/TIDAK ")
kartu = input("apakah kamu membawa kartu pelajar ? IYA/TIDAK ")
hari = input("menonton di hari apa? ")

if umur < 12:
    if 0.5 > diskon: 
        total = 0.5*tiket_normal
        print("Total bayar karena anak-anak ", total)


elif sma == "iya" and kartu == "iya":
    if 0.3 > diskon:
        total = 0.3*tiket_normal
        print("Total bayar karena peljar dan membawa kartu ", total)

elif sma == "iya" and kartu == "tidak":
    print("kamu tidak membawa kartu pelajar tarif ", tiket_normal)

elif hari == "selasa":
    if 0.2 > diskon:
        total = 0.2*tiket_normal
        print("karena kamu nonton di hari selasa tarif jadi ", total)

else:
    print("anda tidak memenuhi diskon yang berlaku", tiket_normal)