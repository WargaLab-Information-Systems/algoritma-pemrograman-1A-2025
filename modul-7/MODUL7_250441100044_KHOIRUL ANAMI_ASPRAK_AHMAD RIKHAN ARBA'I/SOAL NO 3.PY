X = "SOAL NO 3"
print(X)

kupon = {
    "123": 10,
    "345": 20,
    "567": 5
}

def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon yang tersedia.")
    else:
        for kode, diskon in kupon.items():
            print(f"Kode: {kode}, Diskon: {diskon}%")

def proses_transaksi():
    total = float(input("Masukkan total belanja: "))
    kode = input("Masukkan kode kupon: ")

    if kode in kupon:
        diskon = kupon[kode]
        bayar = total - (total * diskon / 100)
        print(f"Selamat diskon {diskon}% diterapkan.")
        print(f"Total bayar: {bayar}")
        del kupon[kode]   
    else:
        print("Kupon tidak valid atau sudah digunakan.")

while True:
    print("\n=== SISTEM KUPON DISKON ===")
    print("1. Tampilkan kupon")
    print("2. Proses transaksi")
    print("3. Keluar")

    pilihanmu = input("Pilih menu: ")

    if pilihanmu == "1":
        tampilkan_kupon()
    elif pilihanmu == "2":
        proses_transaksi()
    elif pilihanmu == "3":
        print("Selamat berbelanja...")
        break
    else:
        print("Input salah.")
