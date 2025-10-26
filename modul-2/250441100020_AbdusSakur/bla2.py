# soal no.3
lama = float(input("berapa jam parkirnya: "))
vip = input("apakah dia member VIP (ya/tidak): ")

if lama != int(lama):
    lama = int(lama) + 1
else:
    lama = int(lama)

if vip == "ya":
    biaya = 0
elif lama <= 2:
    biaya = 5000
else:
    biaya = 5000+(lama-2)*3000


    if biaya  > 20000:
        biaya = 20000


print(F"total biaya parkir: Rp{biaya:,.2f}")