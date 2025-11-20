kupon = {}

def tambah_kupon():
    kode=(input("masukkan kode yang ingin ditambahkan: "))
    if kode in kupon:
        print("kupon sudah tersedia")
        return
    diskon=int(input("masukkan diskon untuk kode kupon(%): "))
    kupon[kode]= diskon
    print("kupon berhasil ditambahkan")

def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon tersedia.\n")
    else:
        for kode, diskon in kupon.items():
            print(f"{kode} diskon {diskon}%")
        print()

def proses_transaksi():
    total = int(input("Total belanja: "))
    pilihan=input("apakah ada kupon (y/n): ").lower()
    if pilihan == "y":
        kode = (input("Masukkan kode kupon: "))
        if kode in kupon:
            potongan = total * kupon[kode] / 100
            bayar = total - potongan
            print(f"Diskon: {int(potongan)}")
            print(f"Total bayar: {int(bayar)}\n")

            del kupon[kode] 
            print("Kupon berhasil digunakan dan kini dihapus.\n")
        else:
            print("Kupon tidak valid atau sudah dipakai.\n")
            print("total belanja :",total)
    elif pilihan == "n":
        print("total belanja :",total)
    else:
        print("pilihan tidak tersedia")

while True:
    print("=== SISTEM KUPON ===")
    print("1. tambah kupon")
    print("2. Tampilkan semua kupon")
    print("3. Proses transaksi")
    print("4. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_kupon()
    elif pilih == "2":
        tampilkan_kupon()
    elif pilih == "3":
        proses_transaksi()
    elif pilih == "4":
        print("Program selesai.terimakasih")
        break
    else:
        print("Pilihan tidak valid.\n")
