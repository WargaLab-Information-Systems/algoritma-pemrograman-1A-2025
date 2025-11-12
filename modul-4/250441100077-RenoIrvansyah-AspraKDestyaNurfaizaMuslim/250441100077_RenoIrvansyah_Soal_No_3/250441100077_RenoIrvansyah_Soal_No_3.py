n = int(input("Masukkan jumlah baris: "))

for i in range(n, 0, -1):

    for kiri in range(1, i + 1):
        print(kiri, end=" ")

    for tengah in range((n - i)):
        print(" ", end=" ")

    for kanan in range(i, 0, -1):
        print(kanan, end=" ")
    
    print()