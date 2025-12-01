def gabung_tuple(t1, t2):
    gabung = t1 + t2
    angka1 = []

    for angka in gabung:
        if angka not in angka1:
            angka1.append(angka)

    n = len(angka1)
    for i in range(n):
        for j in range(0, n - i - 1):
            if angka1[j] < angka1[j+1]:
                angka1[j], angka1[j+1] = angka1[j+1], angka1[j]

    return tuple(angka1)

t1 = (3, 1, 4)
t2 = (1, 5, 9)

hasil = gabung_tuple(t1, t2)
print(hasil)