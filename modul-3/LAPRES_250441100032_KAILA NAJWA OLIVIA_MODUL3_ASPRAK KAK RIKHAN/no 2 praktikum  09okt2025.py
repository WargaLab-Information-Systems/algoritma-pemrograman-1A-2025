pinBenar = "25032"
Maks_percobaan = 3

for percobaan in range(Maks_percobaan):
    pin = input("Masukkan PIN #5digit :")
    if pin == pinBenar:
        print("PIN benar, akses diterima.")
        break
    else:
        if len(str(pin)) > 5:
            print("pin lebih dari 5digit")
        elif len(str(pin)) < 5:
            print("pin kurang dari 5digit")
        SisaAkhir = Maks_percobaan - (percobaan + 1)
        if SisaAkhir > 0:
            print("PIN salah, coba lagi, kesempatan tersisa:", SisaAkhir)
        else:
            print("Akses ditolak, kartu diblokir")