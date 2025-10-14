
nama = input("Nama pembeli:")

total = 0
ulang ="y";
while ulang == "y":
    barang =input("Nama barang: ")
    harga = int(input("Harga barang:"))
    jumlah = int(input("Jumlah barang:"))

    total = total + (harga * jumlah)

    ulang = input("apakah ada pembeli berikutnya? (y/no): ")

print("Nama pembeli:", nama)
print("total belanja: Rp", total)
print("Terima kasih sudah belanja di Indomie!: ")                                       