#Nama = Hari Safira Setyawati
#NIM = 250441100028

print ("Selamat Datang di Kasir Toko Sembako Maju Jaya")

print (input("Masukkan jenis barang yang akan anda beli: "))
#Nama Barang
beras = 12000 
gula = 14000
minyak = 20000
barang = beras + gula + minyak

print (input("Masukkan jumlah barang yang akan anda beli:"))
jenis_barang = 1 + 1 + 1
total_belanja = barang + jenis_barang
print ("Total belanja sementara ", total_belanja)

if total_belanja >= 100000:
    diskon_1 = total_belanja * 0.1
    print ("Anda mendapatkan diskon sebanyak 10%:", diskon_1)
else:
    total_belanja >= 200000
    diskon_2 = total_belanja * 0.
    print ("Anda mendapatkan diskon sebanyak 5%:", diskon_2)

print (input("Apakah anda memiliki member card:"))
if "ya":
    diskon_3 = total_belanja * 0.05
elif "no":
    print ("Anda tidak mendapatkan diskon")

print (input("Apakah ingin melayani pelanggan berikutnya:"))

