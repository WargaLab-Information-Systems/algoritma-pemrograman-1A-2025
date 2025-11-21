def gabung_tuple(t1, t2):
    gabung = list(t1) + list(t2)
    hasil = []
    for i in gabung:
        if i not in hasil:
            hasil.append(i)
    # Urut manual descending
    for i in range(len(hasil)):
        for j in range(i + 1, len(hasil)):
            if hasil[i] < hasil[j]:
                hasil[i], hasil[j] = hasil[j], hasil[i]
    return tuple(hasil)
print("Masukkan elemen tuple pertama (pisahkan dengan spasi):")
t1 = tuple(map(int, input().split()))

print("Masukkan elemen tuple kedua (pisahkan dengan spasi):")
t2 = tuple(map(int, input().split()))
print("Hasil akhir:", gabung_tuple(t1, t2))