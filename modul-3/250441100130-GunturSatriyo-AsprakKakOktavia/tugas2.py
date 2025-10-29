pin_mu = 25130
kesempatan = 3

while kesempatan > 0:
    pin_input = input("Masukkan PIN : ")

    if not pin_input.isdigit():
        print(" PIN harus berupa angka, bukan huruf atau simbol!")
        continue
    pin = int(pin_input)

    if len(pin_input) != 5:
        print(" PIN harus berjumlah 5 digit!")
        continue
    if pin == pin_mu:
        print(" PIN SUKSES BENAR")
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(" PIN MU SALAH! Coba lagi Sisa percobaanmu tinggal :", kesempatan )
        else:
            print(" Akses ditolak, kartu diblokir.")
