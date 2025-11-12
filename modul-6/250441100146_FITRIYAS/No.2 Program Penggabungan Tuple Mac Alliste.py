print("=== Program Gabung Dua Tuple Tanpa Duplikat ===")

# Input tuple pertama
data1 = input("Masukkan elemen tuple pertama (pisahkan dengan spasi): ")
t1 = tuple(map(int, data1.split()))

# Input tuple kedua
data2 = input("Masukkan elemen tuple kedua (pisahkan dengan spasi): ")
t2 = tuple(map(int, data2.split()))

# Gabungkan dua tuple
gabungan = t1 + t2

# Hapus duplikat sambil mempertahankan urutan asli
tanpa_duplikat = []
for angka in gabungan:
    if angka not in tanpa_duplikat:
        tanpa_duplikat.append(angka)

# Urutkan secara menurun (descending) tanpa fungsi bawaan
for i in range(len(tanpa_duplikat)):
    for j in range(i + 1, len(tanpa_duplikat)):
        if tanpa_duplikat[i] < tanpa_duplikat[j]:
            # Tukar posisi
            tanpa_duplikat[i], tanpa_duplikat[j] = tanpa_duplikat[j], tanpa_duplikat[i]

# Ubah kembali menjadi tuple
hasil = tuple(tanpa_duplikat)

# Tampilkan hasil akhir
print("\nTuple hasil akhir (tanpa duplikat & descending):", hasil)
