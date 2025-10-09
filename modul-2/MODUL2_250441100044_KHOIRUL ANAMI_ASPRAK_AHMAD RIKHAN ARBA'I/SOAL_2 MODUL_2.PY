# Soal no 2
X = str("SOAL NO 2")
print (X)
# HARGA NORMAL
harga_normal = 50000

# MASUKKAN 
usia = int(input("Silahkan masukkan usia anda disini ya: "))
pelajar = input("Hai, apakah anda merupakan pelajar SMA dengan kartu pelajar(ya/tidak)?")
hari = input("Silahkan masukkan hari : ")

# VAREABEL UNTUK DISKON
diskon = 0

# CEK KONDISI DISKON
if usia < 12 and usia >= 1:
    if 50 > diskon:
        diskon = 50

if pelajar == "ya"  and usia >= 12: 
    if 30 > diskon:
        diskon = 30

if hari == "selasa":
    if 20 > diskon:
        diskon = 20  

# HITUNG HARGA AKHIR
harga_diskon = harga_normal - (harga_normal * diskon / 100)

# HASIL
if diskon == 0:
    print("Maaf, anda tidak mendapatkan diskon 🤧🤧.")
else:
    print(f"Selamat anda mendapatkan diskon sebesar: {diskon}% 👍👍😊")
    print(f"Jadi harga tiket yang harus kamu bayar sebesar: Rp{int(harga_diskon)}")