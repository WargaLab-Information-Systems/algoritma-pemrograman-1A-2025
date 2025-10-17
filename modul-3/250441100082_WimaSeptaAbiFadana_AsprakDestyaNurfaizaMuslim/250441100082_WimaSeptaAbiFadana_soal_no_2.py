nim = input("masukan 2 nim depan, dan 3 nim terakhir anda : ")
print("jadi PIN anda adalah : ", nim)
pin_benar = nim

kesempatan = 3

while kesempatan > 0:
    pin = input("Masukkan PIN anda : ")

    hanya_angka = True
    for karakter in pin:

        if karakter < "0" or karakter > "9":
            hanya_angka = False
            break

    if not hanya_angka:
        print("PIN harus berupa angka!")
        continue

    if len(pin) != 5:
        print("PIN harus 5 digit!")
        continue

    if pin == pin_benar:
        print("PIN benar, akses diterima.")
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print("PIN salah, coba lagi.")
        else:
            print("Akses ditolak, kartu diblokir.")