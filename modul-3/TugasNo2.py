# Program Simulasi Mesin ATM
PIN_BENAR = "23012"

# User diberi kesempatan 3 kali
kesempatan = 3

while kesempatan > 0:
    pin = input("Masukkan PIN (5 digit): ")

    # Mengecek apakah panjang PIN benar (5 digit)
    if len(pin) != 5 or not pin.isdigit():
        print("PIN harus berupa 5 angka!")
        continue  # Kembali ke awal perulangan

    # Mengecek apakah PIN sesuai
    if pin == PIN_BENAR:
        print("PIN benar, akses diterima.")
        break  # Menghentikan perulangan jika PIN benar
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print("PIN salah, coba lagi.")
        else:
            print("Akses ditolak, kartu diblokir.")