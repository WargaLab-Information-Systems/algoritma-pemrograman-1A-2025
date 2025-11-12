#===== PROGRAM KASIR TOKO SEMBAKO "MAJU JAYA"====

beras = 12000
gula = 14000
minyak = 20000

jumlah_barang = int(input("Masukkan jumlah barang nya: "))
barang = int(input("Masukkan Nama barang yang ingin dibeli: "))
harga = int(input("Harga barang: "))
diskon_membercard =str(input("Apakah pelanggan memiliki member card?(ya/tidak)"))
total = (jumlah_barang * harga )
subtotal = 0 #masih ingin dicari
 
if total < 100000:
    diskon = total - 0.1
if total < 200000:
    diskon = total - 0.05
if subtotal < 150000:
    diskon = subtotal - 0.1
if diskon_membercard == "ya":
    diskon = total - 0.05
else:
    ("tidak ada diskon")

print("\n=== STRUK PERBELANJAAN ===")
print("totalnya adalah: ", total)
print("Total keseluruhannya adalah: ", subtotal)

