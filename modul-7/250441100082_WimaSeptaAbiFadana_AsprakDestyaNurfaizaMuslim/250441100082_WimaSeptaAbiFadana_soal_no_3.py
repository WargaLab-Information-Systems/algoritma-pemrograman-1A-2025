kupon = {}

def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon.")
    else:
        print("\n=== DAFTAR KUPON ===")
        for kode, diskon in kupon.items():
            print("Kode: ", kode, "Diskon: ", diskon, "%")
    print()

def tambah_kupon():
    kode = input("Masukkan kode kupon: ")
    if kode in kupon:
        print("Kupon sudah ada!")
        return

    diskon = int(input("Masukkan persentase diskon: "))
    kupon[kode] = diskon
    print("Kupon berhasil ditambahkan!")

def hapus_kupon():
    kode = input("Masukkan kode kupon: ")
    if kode in kupon:
        del kupon[kode]
        print("Kupon berhasil dihapus!")
    else:
        print("Kupon tidak ditemukan")

def ya(): 
    if not kupon:
        print("Tidak ada kupon tersedia.")
        return

    total = int(input("Masukkan total belanja: "))
    kode = input("Masukkan kode kupon: ")

    if kode not in kupon:
        print("Kupon tidak valid!")
        return

    diskon = kupon[kode]
    potongan = (diskon / 100.0) * total
    total_akhir = total - potongan

    print("Diskon: ", diskon, "%")
    print("Total potongan: ", potongan)
    print("Total bayar setelah diskon: ", total_akhir)

    del kupon[kode]
    print("Kupon telah digunakan")

def tidak():
    total = int(input("masukkan total belanja anda : "))
    print("jadi biaya yang harus anda bayarkan adalah ", total, "karena anda tidak mempunyai kupon diskon")

while True:
    print("=== PROGRAM VALIDASI KUPON ===")
    print("1. Tampilkan kupon")
    print("2. Tambah kupon")
    print("3. Hapus kupon")
    print("4. proses transaksi")

    pilihan = input("Pilih menu (1-4) : ")

    if pilihan == "1":
        tampilkan_kupon()
    elif pilihan == "2":
        tambah_kupon()
    elif pilihan == "3":
        hapus_kupon()
    elif pilihan == "4":
        pilih = input("apakah anda mempunyai kupon diskon atau tidak (ya / tidak) : ")
        if pilih in "ya":
            ya()
        else:
            tidak()
    else:
        print("Pilihan tidak valid!")
