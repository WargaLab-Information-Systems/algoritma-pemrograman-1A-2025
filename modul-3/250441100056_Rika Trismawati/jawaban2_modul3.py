# soal no 2

pin = 25056
kesempatan = 3
while kesempatan > 0:
    n = input ('masukkan PIN anda: ')
    if not n.isdigit() or len(n) != 5:
        print('PIN harus 5 Digit')
        continue 
    if int(n) == pin:
        print('PIN benar, akses di terima')
        break
    else:
        kesempatan -= 1
        if kesempatan == 0:
            print('akses di tolak, kartu di blokir')
            break 
        else:
            print('PIN salah, Coba lagi')
            