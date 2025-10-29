print("="*10,"Program Kasir Maju jaya","="*10)

harga = 0 
total = 0
subtotal = 0 
diskon = 0 
print('''\n ---- Pilihan Menu ----
    a. beras Rp.12000 
    b. Gula Rp. 14000
    c. Minyak Rp.20.000\n''')
while True:
    print("Silahkan Pilih Barang Yang Akan Anda Beli (Ketik selesai Jika Sudah): ")
    barang = input("Masukkan barang : ")
    harga = float(input("harga Barang :"))

    if barang == "selesai":
       break

if harga > 100 :
    diskon = 0.10
elif harga > 200 :
    diskon = 0.15
elif subtotal > 150:
    diskon = 0.10

card = input("Apakah Pelanggan Memiliki Member Card (y/t)").lower()
if card == "y":
    diskon += 0.5
else:
    diskon += 0
total = harga-(harga*diskon)


 

