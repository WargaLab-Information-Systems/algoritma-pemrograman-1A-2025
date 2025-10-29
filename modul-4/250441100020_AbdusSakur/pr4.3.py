n = int(input("Masukan tinggi: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")

    for k in range((n - i)*2):
        print(" ", end=" ")
        
    for l in range(i, 0, -1):
        print(l, end=" ")
    print()
