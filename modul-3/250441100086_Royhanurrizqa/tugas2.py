pin=int(input("silahkan masukkan PIN anda (5 digit) :"))#pin benar 25086
while len(str(pin)) != 5:
    pin=int(input("error= masukkan 5 digit angka :"))
for x in range(3,0,-1):
    if pin == 25086:
        print("PIN benar akses diterima")
        akses=True
        break
    else:
        print("PIN salah,coba lagi")
        print(x,"kesempatan mencoba lagi")
        pin=int(input("PIN anda :"))
        while len(str(pin)) != 5:
            pin=(input("error=masukkan 5 digit angka"))
        akses=False
if akses==False:
    print("Akses ditolak, kartu diblokir")       