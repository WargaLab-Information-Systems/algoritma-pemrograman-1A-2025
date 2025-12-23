vip= input("apakah anda seorang VIP (ya/tidak): ")
if vip == "ya":
    tarif= print("tarif 0 karena anda adalah VIP")
    exit()

lama_parkir= int(input("berapa jam anda parkir : "))
if lama_parkir <= 2:
        tarif= 5000
else:
    tarif= 5000 + (lama_parkir - 2) * 3000

if lama_parkir >= 24:
    tarif= 20000

print("jadi tarifnya adalah : Rp.", tarif)
