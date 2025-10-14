NIM = "250441100110"
PIN = NIM[:2] + NIM[-3:]

kesempatan = 3
percobaan = 0
akses = False

print("=== Selamat datang di ATM ===")

while percobaan < kesempatan:
    masukan = input("Masukkan PIN 5 digit: ")
    percobaan += 1  # setiap input dihitung sebagai percobaan

    # Hitung jumlah karakter dan cek apakah semua karakter angka
    jumlah_karakter = 0
    hanya_angka = True

    for karakter in masukan:
        jumlah_karakter += 1
        if not ('0' <= karakter <= '9'):
            hanya_angka = False
            break

    # Validasi panjang dan jenis karakter
    if jumlah_karakter != 5 or not hanya_angka:
        print("PIN harus berupa 5 digit angka!")
    elif masukan == PIN:
        akses = True
        break
    else:
        print("PIN salah!")

    # Cek apakah sudah 3 kali percobaan
    if percobaan == kesempatan:
        print("Terlalu banyak percobaan! Akses ditolak, kartu diblokir.")
        break
    else:
        print(f"Sisa percobaan: {kesempatan - percobaan}")

# Jika berhasil
if akses:
    print("PIN benar, akses diterima.")