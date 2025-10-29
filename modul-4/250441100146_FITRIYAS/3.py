# Tugas 3 - Pola Dua Piramida Cermin

print("=== Program Pola Dua Piramida Angka ===")

n = int(input("Masukkan jumlah baris: "))

for i in range(n, 0, -1):
    # sisi kiri
    for j in range(1, i + 1):
        print(j, end=" ")
    for l in range(2*(n-i)):
        print (" ",end=" ")
    # sisi kanan (cermin)
    for k in range(i, 0, -1):
        print(k, end=" ")

    print()
