# SOAL NO 4
x = str("SOAL 4")
print(x)

ulang = "iya"

while ulang == "iya":
    print ("Program pembelian indomei")
    nama_pembeli = input("Silahkan masukkan nama pembeli: ")
    total_harga = 0
    daftar_barang = 1

    print("\nSilahkan masukkan data barang (ketik 'selesai' untuk berhenti):")
    while True:
        nama_barang = input(f"Nama barang ke-{daftar_barang}: ")
        if nama_barang.lower() == "selesai":
            break

        harga = int(input(f"Harga {nama_barang}: Rp "))
        total_harga = total_harga + harga 
        daftar_barang = daftar_barang + 1

    print("Nama Pembeli :", nama_pembeli)
    print(f"Total harga pembelian: Rp {total_harga}")
    print("Terima kasih telah berbelanja di IndoMei 😊😊👌")

    ulang = input("Apakah ada pembeli berikutnya? (iya/tidak): ")
    if input != "iya" :
        print("Program selesai. Sampai jumpa!")