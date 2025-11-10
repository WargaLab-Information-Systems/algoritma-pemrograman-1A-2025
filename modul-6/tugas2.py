def gabung_tuple(t1, t2):
    # Gabungkan dua tuple
    gabung = list(t1) + list(t2)
    hasil = []

    # Hapus duplikat, tapi urutan pertama tetap
    for x in gabung:
        if x not in hasil:
            hasil.append(x)

    # Urutkan manual secara menurun (descending)
    for i in range(len(hasil)):
        for j in range(i + 1, len(hasil)):
            if hasil[i] < hasil[j]:
                hasil[i], hasil[j] = hasil[j], hasil[i]

    return tuple(hasil)

# Contoh
t1 = (3, 1, 4)
t2 = (1, 5, 9)
print(gabung_tuple(t1, t2))

