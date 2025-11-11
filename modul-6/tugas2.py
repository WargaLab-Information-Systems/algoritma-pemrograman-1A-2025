def gabung_tuple_dinamis():
    print("Program Gabung Tuple Dinamis")

    t1 = tuple(map(int, input("Masukkan angka): ").split()))

    t2 = tuple(map(int, input("Masukkan angka): ").split()))

    gabung = (t1) + (t2)
    hasil = []

    # hapus duplikat
    for x in gabung:
        if x not in hasil:
            hasil.append(x)

    # urutkan manual (descending karena syarat: hasil[i] < hasil[j])
    for i in range(len(hasil)):
        for j in range(i + 1, len(hasil)):
            if hasil[i] > hasil[j]:
                hasil[i], hasil[j] = hasil[j], hasil[i]

    return tuple(hasil)


print("Hasil:", gabung_tuple_dinamis())


