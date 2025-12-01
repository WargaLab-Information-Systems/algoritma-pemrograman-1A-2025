def main():
    kupon = {
        "gacor": 50
    }

    while True:
        print("============================")
        print("1. Tampilkan Kupon Tersedia")
        print("2. Proses Transaksi")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            if not kupon:
                print("Tidak ada kupon tersedia.")
            else:
                for kode, diskon in kupon.items():
                    print(f"{kode}: {diskon}%")

        elif pilihan == "2":
            total = int(input("Total belanja: "))
            kode = input("Masukkan kode kupon: ")

            if kode in kupon:
                diskon = kupon[kode]
                potongan = total * diskon / 100
                bayar = total - potongan
                print(f"Kupon valid! Diskon {diskon}%")
                print(f"Total bayar: {bayar}")

                del kupon[kode]
                print("Kupon telah digunakan dan dihapus dari sistem.")
            else:
                print("Kupon tidak valid atau sudah digunakan.")
                print(f"Total bayar: {total}")

        elif pilihan == "3":
            break

        else:
            print("Pilihan tidak valid.")

main()
