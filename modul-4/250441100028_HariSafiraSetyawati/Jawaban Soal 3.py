n = int(input("Masukkan tinggi piramida (n): "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")

    for k in range((n - i) * 2):
        print(" ", end=" ")

    for j in range(i, 0, -1):
        print(j, end=" ")

    print() 