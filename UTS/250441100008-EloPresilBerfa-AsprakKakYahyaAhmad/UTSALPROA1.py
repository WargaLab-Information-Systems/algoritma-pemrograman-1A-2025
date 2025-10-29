# Buatlah program Kasir Toko Sembako “Maju Jaya” yang dapat menghitung total belanja pelanggan dengan ketentuan berikut:

# 1. Toko menyediakan 3 jenis barang:
# a. Beras → Rp. 12.000/kg
# b. Gula → Rp. 14.000/kg
# c. Minyak → Rp. 20.000/liter

# 2. Pelanggan bisa membeli lebih dari satu jenis barang (gunakan perulangan untuk menambah item).
# 3. Pelanggan bisa membeli lebih dari satu jumlah barang yang sama
# 4. Jika total belanja lebih dari Rp. 100.000, maka pelanggan mendapat diskon 10%.
# Jika lebih dari Rp. 200.000, maka diskon menjadi 15%. Dan diskon 10% jika Subtotal lebih dari Rp.150.000.00 (Tidak berlaku kelipatan)
# 5. Jika pelanggan memiliki member card, maka mendapat tambahan diskon 5% dari total akhir.
# 6. Setelah satu transaksi selesai, tanyakan apakah ingin melayani pelanggan berikutnya (looping)

# Jawaban
# beras = 12000
# gula = 14000
# minyak = 20000
# print ("Toko Maju Jaya")
# print ("Mau beli apa(Beras, Minyak, Gula)")
# banyak = int(input("Jumlah barang dibeli : "))

# for i in range(banyak):
#     barang = input("Input Nama Barang :").lower()
#     jumlah = int(input("jumlah : "))
    
#     if barang == "beras":
#         total = beras * jumlah
#     elif barang == "gula":
#         total = gula * jumlah
#     elif barang == "minyak":
#         total = minyak * jumlah  
#     print("total : ",total)
#     subtotal = total + total
# print(subtotal)



n = int(input("Masukkan jumlah angka Fibonacci: "))
a, b = 0, 1
print(a, end=" ")
for _ in range(1, n):
    print(b, end=" ")
    a, b = b, a + b

    




    
