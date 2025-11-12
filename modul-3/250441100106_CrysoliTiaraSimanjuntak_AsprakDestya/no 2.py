pin_benar = "12345"
kesempatan = 3

while kesempatan > 0:
    pin = input("Masukkan PIN (5 digit): ")
    if pin == pin_benar:
        print("PIN benar, akses diterima, ")
        break
    else:
        kesempatan -= 1
        if kesempatan == 0:
            print("Akses ditolak, kartu diblokir. ")
        else:
            print("PIN salah, coba lagi. ")                        