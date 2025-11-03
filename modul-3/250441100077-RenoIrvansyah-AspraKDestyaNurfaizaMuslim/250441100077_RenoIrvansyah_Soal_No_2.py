kesempatan = 3
pin_user = 25077

while kesempatan > 0:
        pin = int(input("Masukkan PIN Anda : "))
        if len(str(pin)) != 5:
            print("!!-PIN HARUS 5 DIGIT-!!")
            continue
        if pin == pin_user:
            print("PIN benar, akses diterima")
            break
        else:
            kesempatan -= 1
            if kesempatan > 0:
                print("PIN salah, coba lagi,", kesempatan, " kali")
            else:
                print("Akses ditolak, kartu diblokir")