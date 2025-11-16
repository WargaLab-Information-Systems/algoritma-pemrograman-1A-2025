# Meminta input dua kumpulan angka dari pengguna
tuple1 = tuple(map(int, input("Masukkan angka untuk tuple pertama (pisahkan dengan spasi): ").split()))
tuple2 = tuple(map(int, input("Masukkan angka untuk tuple kedua (pisahkan dengan spasi): ").split()))

gabungan = tuple1 + tuple2
tanpa_duplikat = []
for angka in gabungan:
    if angka not in tanpa_duplikat:
        tanpa_duplikat.append(angka)

# Gunakan algoritma sederhana  range(len(tanpa_duplikat)):
for i in range(len(tanpa_duplikat)):
    for j in range(i + 1, len(tanpa_duplikat)):
        if tanpa_duplikat[i] < tanpa_duplikat[j]:
            tanpa_duplikat[i], tanpa_duplikat[j] = tanpa_duplikat[j], tanpa_duplikat[i]

# Ubah ke bentuk tuple
hasil_akhir = tuple(tanpa_duplikat)

# Tampilkan hasil
print("\nTuple pertama :", tuple1)
print("Tuple kedua   :", tuple2)
print("Hasil akhir   :", hasil_akhir)
