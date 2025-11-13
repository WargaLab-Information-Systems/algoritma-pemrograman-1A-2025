angka1 = (1,2,3,4,5)
angka2 = (2,5,6,7,8)

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