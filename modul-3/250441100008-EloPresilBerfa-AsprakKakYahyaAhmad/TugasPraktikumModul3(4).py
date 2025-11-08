print("="*50)
print("Nama : Elo Presil Berfa")
print("NIM : 250441100008")
print("="*50)

#Soal

#Ambaki adalah seorang developer di sebuah IndoMei. Ambaki diminta untuk membuat program yang menampilkan struk pembelian setiap pelanggan. Program tersebut akan meminta input berupa nama pembeli, daftar barang yang dibeli, dan harga dari setiap barang. Setelah itu, program akan menampilkan struk pembelian yang berisi nama pembeli, daftar barang beserta harganya, total harga keseluruhan, serta pesan “Terima kasih telah berbelanja di IndoMei.” Program akan terus meminta input dari kasir untuk pelanggan berikutnya hingga kasir memasukkan (y/n) pada pertanyaan “Apakah ada pembeli berikutnya?”.

#Jawaban
while True:
    nama = input("Masukkan nama pembeli: ")

    total = 0
    daftar_nama = ""
    daftar_harga = ""

    while True:
        barang = input("Masukkan nama barang (ketik 'selesai' jika sudah): ")
        if barang.lower() == "selesai":
            break
        harga = int(input("Masukkan harga barang: "))

        daftar_nama = daftar_nama + barang + "\n"
        daftar_harga = daftar_harga + "Rp " + str(harga) + "\n"
        total = total + harga

    print("\n===== Struk Pembelian =====")
    print("Nama Pembeli :", nama)
    print("-----------------------------")
    print("Daftar Barang:")
    print(daftar_nama)
    print("Harga:")
    print(daftar_harga)
    print("-----------------------------")
    print("Total Harga : Rp", total)
    print("Terima kasih telah berbelanja di IndoMei.")
    print("=============================\n")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ").lower()
    if lanjut == "n":
        print("Program selesai. Terima kasih!")
        break

print("="*50)