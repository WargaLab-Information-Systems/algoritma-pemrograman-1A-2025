# Buatlah program Kasir Toko Sembako “Maju Jaya” yang dapat menghitung total belanja pelanggan
# dengan ketentuan berikut:

# 1. Toko menyediakan 3 jenis barang:
# a. Beras → Rp. 12.000/kg
# b. Gula → Rp. 14.000/kg
# c. Minyak → Rp. 20.000/liter
# 2. Pelanggan bisa membeli lebih dari satu jenis barang (gunakan perulangan untuk menambah item).
# 3. Pelanggan bisa membeli lebih dari satu jumlah barang yang sama
# 4. Jika total belanja lebih dari Rp. 100.000, maka pelanggan mendapat diskon 10%.
# Jika lebih dari Rp. 200.000, maka diskon menjadi 15%. Dan diskon 10% jika Subtotal lebih dari Rp.
# 150.000.00 (Tidak berlaku kelipatan)
# 5. Jika pelanggan memiliki member card, maka mendapat tambahan diskon 5% dari total akhir.
# 6. Setelah satu transaksi selesai, tanyakan apakah ingin melayani pelanggan berikutnya (looping)
# 7. Dibuat secara kompleks (memperhitungkan setiap kondisi benar/salah)


# 8. Gunakan Tools VSCode
# 9. MATIKAN Internet dan DISABLE Extension VSCode.
# Pengumpulan melalui Classroom dan Github dengan penamaan file rar/zip: UTS_ALPRO1A_NIM_NAMA
# Contoh: UTS_ALPRO1A_25-079_BUDI PEKERTI
# File berisi Code, Screenshoot, dan README (Penjelasan)

while True:
        barang = input("Masukkan nama barang (atau ketik 'selesai' jika sudah selesai): ")
        if barang.lower() == 'selesai':
            break

        while True:
            harga = int(input(f"Masukkan harga {barang}: Rp "))
            if harga < 0:
                print(" Harga harus positif !!! Silakan masukkan lagi.")
            else:
                break








    


