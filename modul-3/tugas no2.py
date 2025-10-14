PIN_BENAR = 12567

for i in range(3):
    pin = input("Masukkan PIN (5 digit): ")

    if pin == "12567":
        print("PIN benar, akses diterima.")
        break
    elif len(pin) != 5 :
        print("PIN harus berupa angka 5 digit!\n")
    else:
        print("PIN salah, coba lagi.\n")
else:
    print("Akses ditolak, kartu diblokir.")