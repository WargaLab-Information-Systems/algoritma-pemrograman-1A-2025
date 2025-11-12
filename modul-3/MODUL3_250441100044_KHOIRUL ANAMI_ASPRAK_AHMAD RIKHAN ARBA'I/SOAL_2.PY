# SOAL NO 2
x = str("SOAL 2")
print(x)

pin_sebenarnya = input("Silahakan masukkan PIN anda yang sebenarnya (5 digit): ")

jumlah_digit = 0
hanya_angka = True

for karakter in pin_sebenarnya:
    jumlah_digit += 1
    if karakter not in "0123456789":
        hanya_angka = False

if jumlah_digit != 5 or not hanya_angka:
    print("Maaf, PIN harus terdiri dari 5 angka🥹.")
else:
    percobaan = 0

    while percobaan < 3:
        pin_input = input("Masukkan PIN Anda: ")
        if pin_input == pin_sebenarnya:
            print("PIN anda benar, akses diterima😁😊.")
            break
        else:
            percobaan += 1
            if percobaan < 3:
                print("PIN anda salah🤧, coba lagi.")
            else:
                print("Akses ditolak, kartu anda diblokir😒.")
