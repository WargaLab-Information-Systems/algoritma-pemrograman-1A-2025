pinbenar = 25020
kesempatan = 3

while kesempatan > 0:
    try:
        pin = int(input("Masukkan PIN 5 digit angka: "))
        if len(str(pin)) != 5:
            print("PIN harus tepat 5 digit angka. Coba lagi")
            continue

        if pin == pinbenar:
            print("pin benar, akses diterima")
            break
        else:
            kesempatan -= 1
            print("pin salah. coba lagi")
    except ValueError:
        print("pin harus berupa angka. coba lagi")
if kesempatan == 0:
    print("akses ditolak. Kartu diblokir")