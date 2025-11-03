pinBenar = "25024"
Maks_percobaan = 3

for percobaan in range(Maks_percobaan):
    pin = input("Masukkan PIN #5digit :")
    if pin == pinBenar:
        print("PIN benar, akses diterima.")
        break
    else:
        SisaAkhir = Maks_percobaan - (percobaan + 1)
        if SisaAkhir > 0:
            print("PIN salah, coba lagi, kesempatan tersisa:", SisaAkhir)
        else:
            print("Akses ditolak, kartu diblokir")