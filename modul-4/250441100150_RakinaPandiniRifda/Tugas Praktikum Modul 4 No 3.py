n = int(input("Masukkan tinggi piramida (n): "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(f"{j:2}", end="")
    for k in range(1, (n - i) * 4 + 1):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(f"{j:2}", end="")
    print()