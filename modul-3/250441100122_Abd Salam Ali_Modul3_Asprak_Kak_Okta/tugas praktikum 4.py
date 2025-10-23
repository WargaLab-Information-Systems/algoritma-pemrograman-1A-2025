while True:
    print("\n=== Program Struk Pembelian IndoMei ===")

    nama = input("Masukkan nama pembeli: ")

    # Daftar barang dan harga
    daftar_barang = []
    daftar_harga = []
    total_harga = 0

    while True:
        # Input barang dan harga
        barang = input("Masukkan nama barang (ketik 'selesai' jika sudah): ")
        if barang.lower() == "selesai":
            break

        # Validasi harga (tidak boleh huruf)
        while True:
            harga_input = input(f"Masukkan harga untuk {barang}: ")

            hanya_angka = True
            for karakter in harga_input:
                if karakter < '0' or karakter > '9':   # cek satu per satu
                    hanya_angka = False
                    break

            if not hanya_angka or harga_input == "":
                print("Harga harus berupa angka! Silakan coba lagi.")
            else:
# ubah ke integer manual (tanpa int())
                harga = 0
                for karakter in harga_input:
                    harga = harga * 10 + (ord(karakter) - ord('0'))
                break

        daftar_barang.append(barang) # menambahkan barang ke list
        daftar_harga.append(harga)
        total_harga += harga

    # Cetak struk
    print("          STRUK PEMBELIAN")
    print(f"Nama Pembeli : {nama}")
    print("Daftar Barang:")
    for i in range(len(daftar_barang)):
        print(f"{i+1}. {daftar_barang[i]} - Rp{daftar_harga[i]}")
    print(f"Total Harga  : Rp{total_harga}")
    print("Terima kasih telah berbelanja di IndoMei.")
# Tanya apakah ada pembeli berikutnya
    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lanjut.lower() != "y":
        print("\nProgram selesai. Terima kasih!")
        break

