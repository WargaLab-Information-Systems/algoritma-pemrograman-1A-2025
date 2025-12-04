X = ("SOAL NO 2")
print(X)


data1 = (3, 1, 4)
data2 = (1, 5, 9)

gabung = data1 + data2

tampung = []

for angka in gabung:
    if angka not in tampung:
        tampung.append(angka)

for i in range(len(tampung)):
    for j in range( i + 1, len(tampung) ):
        if tampung[i] < tampung[j]:
            tampung[i], tampung[j] = tampung[j], tampung[i]

hasil = tuple(tampung)

print ("Jadi hasil akhirnya menjadi", hasil)