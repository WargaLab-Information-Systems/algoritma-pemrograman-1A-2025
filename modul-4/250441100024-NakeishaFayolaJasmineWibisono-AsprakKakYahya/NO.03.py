n = int(input("Masukkan angka n: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
        
    space = (n - i) * 2
    print(" " * space, end="")
    
    for j in range(i, 0, -1):
        print(j, end="")

    print()
    