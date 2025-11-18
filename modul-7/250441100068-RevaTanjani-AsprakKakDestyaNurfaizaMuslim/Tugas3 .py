kupon = {
    "DISKON": 10,
    "HEMAT": 20,
    "AKUCINTAPRAKTIKUM": 50
}

def cek():
    if len(kupon) == 0:
        print("\nTidak ada kupon tersedia.")
    else:
        print("\n=== Daftar Kupon ===")
        for kode, diskon in kupon.items():
            print(f"Kode: {kode} | Diskon: {diskon}%")

def transaksi():
    total = float(input("Masukkan total belanja: "))
    kode = input("Masukkan kode kupon: ").upper()

    if kode in kupon:
        diskon = kupon[kode]
        potongan = total * diskon / 100
        bayar = total - potongan

        print(f"Kupon valid! Diskon {diskon}%")
        print(f"Total potongan: Rp{potongan}")
        print(f"Total bayar: Rp{bayar}")

        del kupon[kode]  
    else:
        print("Kupon tidak valid atau sudah dipakai.")
        print(f"Total bayar: Rp{total}")

while True:
    print("| 1. cek | 2.transaksi | 3.keluar |")
    pilih = input("Pilih menu: ")

    if pilih == "1" or pilih == "cek": cek()
    elif pilih == "2" or pilih == "transaksi":transaksi()
    elif pilih == "3" or pilih == "keluar ":
        break
    else:
        print("Menu tidak valid!")
