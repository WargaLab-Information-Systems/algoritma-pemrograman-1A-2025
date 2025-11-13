angka1 =tuple(map(int, input("Masukkan data tuple pertama (pisah dengan spasi): ").split()))
angka2 =tuple(map(int, input("Masukkan data tuple Kedua (pisah dengan spasi): ").split()))

gabungan = angka1 + angka2

aseli = []
for angka in gabungan:
    if angka not in aseli:
        aseli.append(angka)

for i in range(len(aseli)):
    for j in range(i + 1, len(aseli)):
        if aseli[i] < aseli[j]:
            aseli[i], aseli[j] = aseli[j], aseli[i]

hasil = tuple(aseli)
print(f"Hasil: {hasil}")