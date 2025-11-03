kesempatan = 3
while True:
    pin = input("Masukkan PIN (5 digit): ")
    if kesempatan == 0:
        print("Akses ditolak, kartu diblokir")
        break
    kesempatan -= 1
    if not pin.isdigit() or len(pin) != 5:
        print("PIN harus berupa 5 digit angka!")
        continue
    else:
        print("PIN benar, akses diterima")
        break
    