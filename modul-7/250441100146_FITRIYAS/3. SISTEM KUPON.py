kupon = {
    "PROMO10": 10,
    "HEMAT20": 20,
    "DISKON50": 50
}

def input_float(pesan):
    while True:
        nilai = input(pesan)
        try:
            return float(nilai)
        except:
            print("ERROR: Input harus berupa angka!")

def menu_input():
    while True:
        pilih = input("Pilih menu (1-3): ")
        if pilih.isdigit() and 1 <= int(pilih) <= 3:
            return int(pilih)
        print("ERROR: Pilihan harus angka 1-3!")

def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon tersisa.")
    else:
        print("\n=== DAFTAR KUPON ===")
        for kode, diskon in kupon.items():
            print(f"{kode} : {diskon}%")

def proses_transaksi():
    total = input_float("Masukkan total belanja: ")
    kode = input("Masukkan kode kupon: ")

    if kode in kupon:
        diskon = kupon[kode]
        potongan = total * (diskon / 100)
        total_bayar = total - potongan
        print(f"Kupon valid! Diskon {diskon}%")
        print(f"Total yang harus dibayar: {total_bayar}")
        del kupon[kode]   # kupon dihapus setelah digunakan
    else:
        print("ERROR: Kupon tidak valid atau sudah digunakan.")

while True:
    print("\n=== SISTEM KUPON DISKON ===")
    print("1. Tampilkan semua kupon")
    print("2. Proses transaksi menggunakan kupon")
    print("3. Keluar")

    pilihan = menu_input()

    if pilihan == 1:
        tampilkan_kupon()
    elif pilihan == 2:
        proses_transaksi()
    elif pilihan == 3:
        print("Program selesai.")
        break
