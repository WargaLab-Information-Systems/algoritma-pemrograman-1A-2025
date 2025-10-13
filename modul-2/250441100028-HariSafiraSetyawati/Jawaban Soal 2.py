harga_normal = 50000
usia = int(input("Masukkan usia anda: "))
status_pelajar = input("Apakah anda pelajar SMA? (ya/tidak): ").lower()
hari = input("Masukkan hari kunjungan (Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu): ")
if usia < 12:
    diskon = 0.5
elif status_pelajar == "ya":
    diskon = 0.3
elif hari == "selasa":
    diskon = 0.2
else:
    diskon = 0

persen = int(diskon * 100)
harga_diskon = harga_normal * diskon

print("Harga tiket masuk: Rp", harga_normal)
print("Diskon mendapatkan nilai: ", persen, "%")
print("Harga yang harus dibayar: Rp", harga_diskon)