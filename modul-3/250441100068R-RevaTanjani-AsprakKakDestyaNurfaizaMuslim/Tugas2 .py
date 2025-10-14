a = 0
b = "25068"
while a < 3:
    pin = input("masukkan PIN ")
    if len(pin) != 5 or not pin.isdigit():
        print("================")
        print("Input tidak sesuai format")
        print("================")
        continue
    if pin == b:
        print("PIN benar, akses diterima")
        break
    else:
         print("================")
         print("PIN salah, coba lagi")
         print("================")
         a += 1
if a == 3:
    print("Akses ditolak, kartu diblokir")
    print("================")