ulang = "y"
barang_lagi = "y"
harga = 0
diskon = 0
while barang_lagi == "y":
    jenis_barang= input("masukkan jenis barang: ")
    if jenis_barang == "beras":
     harga_barang = 12000
    elif jenis_barang == "gula":
        harga_barang = 14000
    elif jenis_barang == "minyak":
        harga_barang = 20000
    barang_lagi = input("apakah ada barang lagi? ")
    harga += harga_barang
 
    if harga > 100000:
       diskon = 0.10
    elif harga > 200000:
       diskon = 0.20
    else: 
       print("diskon 0")

















# if jenis_barang == "beras":
#     harga_barang = 12000
# elif jenis_barang == "gula":
#     harga_barang = 14000
# elif jenis_barang == "minyak":
#     harga_barang = 20000