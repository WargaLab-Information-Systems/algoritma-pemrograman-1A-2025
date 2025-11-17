# Program Validasi Kupon Diskon untuk Sistem Kasir

kupon = {
    "DISC10": 10,
    "HEMAT20": 20,
    "SUPER30": 30
}

def tampilkan_kupon():
    if not kupon:
        print("\nTidak ada kupon yang tersedia.\n")
        return
    
    print("\n=== Daftar Kupon yang Tersedia ===")
    for kode, diskon in kupon.items():
        print(f"Kode Kupon : {kode} | Diskon : {diskon}%")
    print()

def proses_transaksi():
    try:
        total_belanja = float(input("Masukkan total belanja: "))
    except ValueError:
        print("Total belanja harus berupa angka!\n")
        return
    
    kode = input("Masukkan kode kupon (atau tekan Enter jika tidak memakai): ").strip()

    if kode == "":
        print(f"Total yang harus dibayar: Rp {total_belanja:}\n")
        return

    if kode not in kupon:
        print("Kupon tidak valid atau sudah digunakan!\n")
        return

    diskon = kupon[kode]
    potongan = total_belanja * (diskon / 100)
    total_bayar = total_belanja - potongan

    print(f"\nKupon valid! Diskon {diskon}% diterapkan.")
    print(f"Total belanja     : Rp {total_belanja:}")
    print(f"Potongan diskon   : Rp {potongan:}")
    print(f"Total harus bayar : Rp {total_bayar:}\n")

    del kupon[kode]
    print("Kupon berhasil digunakan dan telah dihapus dari sistem.\n")

# ===== MENU UTAMA =====
while True:
    print("=== MENU SISTEM KUPON DISKON ===")
    print("1. Tampilkan semua kupon")
    print("2. Proses transaksi dengan kupon")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        tampilkan_kupon()
    elif pilihan == "2":
        proses_transaksi()
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.\n")