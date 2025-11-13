pin_benar = 25004 
kesempatan = 3

for i in range(0, 3):
    pin = int(input("Masukkan PIN (5 digit): "))
    if pin == pin_benar:
        print("PIN benar, akses diterima.")
        break
    else:
        print("PIN salah, coba lagi!")
else:
    print("Akses ditolak, kartu diblokir.")