
t1 = tuple(map(int, input("Masukkan elemen tuple pertama (pisahkan dengan spasi): ").split()))
t2 = tuple(map(int, input("Masukkan elemen tuple kedua (pisahkan dengan spasi): ").split()))

gabungan = t1 + t2

unik = []
for angka in gabungan:
    if angka not in unik:
        unik.append(angka)

for i in range(len(unik)):
    for j in range(i + 1, len(unik)):
        if unik[i] < unik[j]:
            unik[i], unik[j] = unik[j], unik[i]

hasil = tuple(unik)
print("Hasil:", hasil)
