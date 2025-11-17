tuple1 = tuple(map(int, input("Masukkan angka untuk tuple pertama (pisahkan dengan spasi): ").split()))
tuple2 = tuple(map(int, input("Masukkan angka untuk tuple kedua (pisahkan dengan spasi): ").split()))

gabung = tuple1 + tuple2

hasil_tanpa_duplikat = []
for angka in gabung:
    if angka not in hasil_tanpa_duplikat:
        hasil_tanpa_duplikat.append(angka)
hasil_urut = []
while hasil_tanpa_duplikat:
    terbesar = max(hasil_tanpa_duplikat)   # cari angka terbesar
    hasil_urut.append(terbesar)            # masukkan ke hasil
    hasil_tanpa_duplikat.remove(terbesar)  # hapus dari list asal

# 4. Kembalikan ke bentuk tuple
hasil_akhir = tuple(hasil_urut)

# Output
print("\nTuple pertama :", tuple1)
print("Tuple kedua   :", tuple2)
print("Hasil akhir   :", hasil_akhir)



