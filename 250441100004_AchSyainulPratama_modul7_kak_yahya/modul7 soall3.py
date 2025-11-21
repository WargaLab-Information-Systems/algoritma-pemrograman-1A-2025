def sistem_kasir():
    kupon = {'DISKON10': 10, 'HEMAT20': 20, 'MERDEKA': 15}

    def tampilkan_kupon():
        if not kupon:
            print("Tidak ada kupon yang tersedia.")
        else:
            print("\nDaftar Kupon:")
            for kode, diskon in kupon.items():
                print(f"Kode: {kode}, Diskon: {diskon}%")

    def proses_transaksi(total_belanja, kode_kupon):
        if kode_kupon in kupon:
            diskon = kupon[kode_kupon]
            total_diskon = total_belanja * (diskon / 100)
            total_bayar = total_belanja - total_diskon
            del kupon[kode_kupon]
            print(f"Total belanja: {total_belanja}")
            print(f"Diskon: {diskon}%")
            print(f"Total yang harus dibayar setelah diskon: {total_bayar}")
            print("Kupon berhasil digunakan dan dihapus.")
        else:
            print("Kupon tidak valid atau sudah digunakan.")

    while True:
        print("\nMenu:")
        print("1. Tampilkan Kupon")
        print("2. Proses Transaksi")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            tampilkan_kupon()
        elif pilihan == '2':
            total_belanja = float(input("Masukkan total belanja: "))
            kode_kupon = input("Masukkan kode kupon: ")
            proses_transaksi(total_belanja, kode_kupon)
        elif pilihan == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

# Inisialisasi program
sistem_kasir()