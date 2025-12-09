kupon = {
    "wongireng":0.5,
    "jmk48":0.7,
    "priahytam":1
}

def tampilkan_kupon():
    print("\nDaftar Kupon Diskon:")
    for kode, diskon in kupon.items():
        print(f"Kode: {kode}, Diskon: {int(diskon * 100)}%")

def proses_transaksi():
    total_belanja = int(input("Masukkan total belanja: "))
    kode = input("Masukkan kode kupon: ").lower()

    if kode in kupon:
        diskon = kupon[kode]
        jumlah_diskon = total_belanja * diskon
        total_bayar = total_belanja - jumlah_diskon
        print(f"Diskon yang didapat: {int(diskon * 100)}%")
        print(f"Jumlah diskon: Rp{int(jumlah_diskon)}")
        print(f"Total yang harus dibayar: Rp{int(total_bayar)}")
        del kupon[kode]
        print("Kupon telah digunakan dan dihapus dari daftar kupon.")
    else:
        print("Kode kupon tidak valid.")

while True:
    print("\n===== Sistem Kupon Diskon =====")
    print("1. Tampilkan Semua Kupon")
    print("2. Proses Transaksi dengan Kupon")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        tampilkan_kupon()
    elif pilihan == "2":
        proses_transaksi()
    elif pilihan == "3":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid.")