# rika trismawati
# nim 250441100056

# 3 jenis jumlah barang 

pelanggan =int(input("Memasukkan barang yang ingin kita beli:"))
beras    = 1
gula     = 1
minyak   = 1
pelanggan = 100
diskon = 10

# harga barang 
beras = 12000 
gula = 14000
minyak = 20000

total_harga =(1* beras + 1 *gula + 1 *minyak)
print=("total harga beras* 12000:",beras* 12000)
print=("total harga minyak * 12000:",minyak* 14000)
print=("total harga gula* 12000:",gula* 2000)

if pelanggan > 100:
    print("maka pelanggan mendapatkan diskon 10%:",)
elif pelanggan < 100:
    print("maka pelanggan tidak mendapatkan diskon:",)
else:
    print("tidak ada diskon:",)
