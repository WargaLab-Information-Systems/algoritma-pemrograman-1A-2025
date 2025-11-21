# Program Validasi Kupon Diskon
# Format penyimpanan:
# kupon = { "KODE": persentase_diskon }
kupon = {
    "HEMAT10": 10,
    "DISKON20": 20,
    "SALE30": 30
}
def tampilkan_kupon():
    if not kupon:
        print("\nTidak ada kupon yang tersedia.\n")
    else:
        print("\n=== DAFTAR KUPON TERSEDIA ===")
        for kode, diskon in kupon.items():
            print(f"Kode : {kode} | Diskon : {diskon}%")
        print()
def proses_transaksi():
    total_belanja = float(input("Masukkan total belanja: "))
    kode = input("Masukkan kode kupon: ")
    if kode not in kupon:
        print("\nKupon tidak valid atau sudah digunakan!\n")
        return
    diskon = kupon[kode]
    potongan = total_belanja * (diskon / 100)
    total_bayar = total_belanja - potongan

    print("\n=== RINCIAN PEMBAYARAN ===")
    print(f"Total Belanja      : Rp {total_belanja}")
    print(f"Diskon ({diskon}%) : Rp {potongan}")
    print(f"Total Bayar        : Rp {total_bayar}\n")

    del kupon[kode]
    print("Kupon berhasil digunakan dan telah dihapus!\n")

# ========================
#       MENU UTAMA
# ========================
while True:
    print("=== SISTEM KASIR - KUPON DISKON ===")
    print("1. Tampilkan Semua Kupon")
    print("2. Proses Transaksi dengan Kupon")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")
    if pilihan == "1":
        tampilkan_kupon()
    elif pilihan == "2":
        proses_transaksi()
    elif pilihan == "3":
        print("\nProgram selesai. Terima kasih!\n")
        break
    else:
        print("\nPilihan tidak valid. Coba lagi.\n")