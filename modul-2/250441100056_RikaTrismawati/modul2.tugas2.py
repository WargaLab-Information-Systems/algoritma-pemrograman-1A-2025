# Soal no 2
# HARGA NORMAL
harga_normal = 50000

# MASUKKAN 
usia = int(input("Silahkan masukkan usia anda disini ya: "))
pelajar = input("apakah anda merupakan pelajar SMA dengan kartu pelajar(iya/tidak)?")
hari = input("Silahkan masukkan hari : ")

# ini adalah variabel untuk diskon
diskon = 0

# cek kondisi diskonnya
if hari == "selasa":
    diskon1 = 0.2*harga_normal # 20% * 50 =15.000
    total = harga_normal- diskon1
    print("diskon di hari selasa ", total) 

if usia < 12 and usia >= 1:
    diskon2 = 0.5*harga_normal
    total = harga_normal-diskon2
    print("karena anak - anak ", total)

    if usia < 12 and usia >= 1 and hari == "selasa":
        total = harga_normal-(diskon1+diskon2)
        print("diskon karena anak-anak dan di hari selasa", total)

if pelajar == "iya"  and usia >= 12:
    diskon2 = 0.3*harga_normal
    total = harga_normal-diskon2
    print("jadi diskonnya karena anda merupakan pelajar sma ", total)

    if pelajar == "iya"  and usia >= 12 and hari == "selasa": 
        total = diskon1+diskon2
        print("maka total diskon karena anda pelajar dan nonton di hari selasa ", total)
