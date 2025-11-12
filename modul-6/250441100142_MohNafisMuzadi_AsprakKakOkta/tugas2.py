t1 = tuple(map(int, input("Masukkan data tuple pertama (pisahkan dengan spasi): ").split()))
t2 = tuple(map(int, input("Masukkan data tuple kedua (pisahkan dengan spasi): ").split()))

hasil = tuple(set(t1 + t2))

for i in range(len(hasil)):
    for j in range(i + 1, len(hasil)):
        if hasil[i] < hasil[j]:
            simpan = list(hasil)
            simpan[i], simpan[j] = simpan[j], simpan[i]
            hasil = tuple(simpan)

print(hasil)
