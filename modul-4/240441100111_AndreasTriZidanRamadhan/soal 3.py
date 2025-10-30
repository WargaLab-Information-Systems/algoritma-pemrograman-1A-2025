n = int(input("Masukkan tinggi piramida: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    
    spasi = (n - i) * 2
    print(" " * spasi, end="")
    
    for k in range(i, 0, -1):
        print(k, end="")
    
    print()  

