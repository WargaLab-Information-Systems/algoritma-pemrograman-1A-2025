pin_saya = "25146"
kesempatan = 3

for i in range(kesempatan):
    pin = input("masukkan pin (5 digit) : ")
    while len(str(pin)) != 5:
        pin=int(input("error= masukkan 5 digit angka :"))
    if pin == pin_saya:
        print("PIN benar, akses diterima")
        break
    else:
        print("PIN salah, coba lagi")
else:
    print("akses ditoloak, kartu diblokir")