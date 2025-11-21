# Menampilkan database kupon beserta persentase diskon
kupon = {"discn10": 10, "discn20": 20, "discn30": 30}

def input_menu():
    while True:
        try:
            pilihan = int(input("Pilih menu (1-3): "))
            if 1 <= pilihan <= 3:
                return pilihan
            else:
                print("Pilihan harus antara 1 sampai 3!")
        except ValueError:
            print("Input harus berupa angka! Coba lagi.")

def input_total():
    while True:
        try:
            total = float(input("Masukkan total belanja: "))
            if total < 0:
                print("Total belanja tidak boleh negatif!")
            else:
                return total
        except ValueError:
            print("Total belanja harus berupa angka! Coba lagi.")

def input_kode():
    while True:
        kode = input("Masukkan kode kupon: ")
        try:
            if kode == "":
                raise ValueError
            return kode
        except ValueError:
            print("Kode kupon tidak boleh kosong! Coba lagi.")
#read
def tampilkan_kupon(kupon):
    if not kupon:
        print("Tidak ada kupon yang tersedia.\n")
        return
    print("Daftar Kupon yang Tersedia:")
    for k, d in kupon.items():
        print(f"Kode: {k} | Diskon: {d}%")
    print()

def proses_transaksi(kupon):
    if not kupon:
        print("Tidak ada kupon yang bisa digunakan.\n")
        return
    
    #read
    total = input_total()
    kode = input_kode()

    if kode not in kupon:
        print("Kupon tidak valid atau sudah digunakan.\n")
        return

    diskon = kupon[kode]
    potongan = total * diskon / 100

    #update
    total_akhir = total - potongan

    print(f"\nKupon valid! Diskon {diskon}% diterapkan.")
    print(f"Total sebelum diskon : Rp{total}")
    print(f"Potongan             : Rp{potongan}")
    print(f"Total dibayar        : Rp{total_akhir}")

    #delete atau menghapus kupon setelah digunakan
    del kupon[kode]
    print("Kupon telah digunakan dan dihapus.\n")

while True:
    print("=== Sistem Kupon Diskon ===")
    print("1. Tampilkan semua kupon")
    print("2. Proses transaksi dengan kupon")
    print("3. Keluar")

    pilihan = input_menu()

    if pilihan == 1:
        tampilkan_kupon(kupon)
    elif pilihan == 2:
        proses_transaksi(kupon)
    elif pilihan == 3:
        print("Terima kasih! Program selesai.")
        break