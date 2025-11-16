n = int(input("Masukkan nilai n: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")

    for s in range((n - i) * 4):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end=" ")
    print()