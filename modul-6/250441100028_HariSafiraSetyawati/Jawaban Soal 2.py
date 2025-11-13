t1 = input("Masukkan nilai pertama: ").split(",")
t2 = input("Masukkan nilai kedua: ").split(",")

gabungan = t1 + t2

hasil = []
for nilai in gabungan:
    ada = False
    for x in hasil:
        if x == nilai:
            ada = True
            break
    if not ada:
        hasil.append(nilai)

for i in range(len(hasil)):
    for j in range(i + 1, len(hasil)):
        if hasil[i] < hasil[j]:
            temp = hasil[i]
            hasil[i] = hasil[j]
            hasil[j] = temp

hasil_akhir = tuple(hasil)
print("Hasil akhir:", hasil_akhir)