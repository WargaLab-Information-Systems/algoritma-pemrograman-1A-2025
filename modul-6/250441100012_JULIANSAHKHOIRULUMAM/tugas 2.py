print("="*10, " TUGAS 2 MODUL 6 ", "="*10)

nilai1 = input("Masukkan nilai pertama (pisahkan dengan koma): ").split(",")
nilai2 = input("Masukkan nilai kedua  (pisahkan dengan koma): ").split(",")

gabungan = nilai1 + nilai2

# Hapus nilai yang duplikat
nilai = []
for n in gabungan:
    if n not in nilai:
        nilai.append(n)

# Urutkan dari terbesar ke terkecil
for i in range(len(nilai)):
    for j in range(i + 1, len(nilai)):
        if nilai[i] < nilai[j]:
            # Tukar posisi
            nilai[i], nilai[j] = nilai[j], nilai[i]

# Ubah hasil akhir menjadi tuple
hasil_akhir = tuple(nilai)

print("Hasil akhir:", hasil_akhir)
