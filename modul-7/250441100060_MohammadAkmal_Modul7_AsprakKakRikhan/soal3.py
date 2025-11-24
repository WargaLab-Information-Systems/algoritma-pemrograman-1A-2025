kupon = {
    "HEMAT BELANJA" : 10,
    "DISKON MURAH"  : 35,
    "PROMO SPECIAL" : 50,
    "SPECIAL SELL"  : 80
}

def tampilkan_kupon():
    if not kupon:
        print("\nTidak ada kupon yang tersisa.\n")
        return

    print("\n=== Daftar Kupon Tersedia ===")
    for kode, persen in kupon.items():
        print(f"{kode} -> {persen}%")
    print()

def proses_transaksi():
    try:
        total = float(input("Total belanja: "))
    except ValueError:
        print("Input tidak valid.\n")
        return

    kode = input("Masukkan kode kupon : ").strip()

    if kode == "":
        print(f"Total yang harus dibayar : Rp{total:.2f}\n")
        return

    if kode not in kupon:
        print("Kupon tidak ditemukan atau sudah dipakai.\n")
        return

    diskon = kupon[kode]
    potongan = total * (diskon / 100)
    bayar = total - potongan

    print(f"Kupon valid! Diskon {diskon}%")
    print(f"Potongan        : Rp{potongan:.2f}")
    print(f"Total bayar     : Rp{bayar:.2f}\n")

    kupon.pop(kode)

def menu():
    while True:
        print("=== MENU KUPON DISKON ===")
        print("1. Tampilkan kupon tersedia")
        print("2. Proses transaksi")
        print("3. Keluar")

        pilih = input("Pilih menu (1-3): ").strip()

        if pilih == "1":
            tampilkan_kupon()
        elif pilih == "2":
            proses_transaksi()
        elif pilih == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.\n")

menu()