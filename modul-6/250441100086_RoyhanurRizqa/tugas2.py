t1 = tuple(map(int, input("Masukkan angka tuple ke-1 (pisah dengan spasi): ").split()))
t2 = tuple(map(int, input("Masukkan angka tuple ke-2 (pisah dengan spasi): ").split()))

gabung = t1 + t2
benar = []

for i in gabung:
    ada = True
    for u in benar:
        if u == i:
            ada = False
            break
    if ada:
        benar.append(i)

panjang = 0
for k in benar:
    panjang += 1

for i in range(panjang):
    j = i + 1
    while j < panjang:
        if benar[i] < benar[j]:
            benar[i], benar[j] = benar[j], benar[i]
        j += 1
 
hasil = tuple(benar)
print("Hasil akhir:", hasil)
