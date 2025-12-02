pin_benar = 25060
kesempatan = 3

while kesempatan > 0:
    pin_masuk = int(input("Masukkan PIN (5 digit): "))
    if pin_masuk == pin_benar:
        print("PIN benar. Akses diterima.")
        break
    else:
        print("PIN salah, coba lagi.")
        kesempatan = kesempatan - 1
if kesempatan == 0:
    print("Akses ditolak. PIN anda di blokir")