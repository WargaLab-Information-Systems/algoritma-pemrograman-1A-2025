harga_tiket = 50000
diskon = 0

usia = int(input("Masukkan usia penonton: "))
if usia < 12:
    diskon = max(diskon, 0.50)
elif usia > 12:
    status = input("Apakah pelajar SMA dan membawa kartu pelajar ? (ya/tidak): ").lower()
    if status == "ya":
        diskon = max(diskon, 0.30)

hari = input("Menonton hari (Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu): ").lower()
if hari == "selasa":
    diskon = max(diskon, 0.20)
else:
    diskon = max(diskon, 0)
harga_setelah_diskon = harga_tiket - (harga_tiket * diskon)

print("Harga tiket awal", harga_tiket)
print("Diskon yang didapat : ", int(diskon*100), "%")
print("Harga tiket setelah diskon : Rp", int(harga_setelah_diskon))