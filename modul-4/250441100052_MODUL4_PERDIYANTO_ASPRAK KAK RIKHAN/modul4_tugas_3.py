baris = int(input("Masukkan jumlah baris: "))

for i in range(baris, 0, -1):
    
    for j in range(1, i + 1):
        print(j, end="")
 
    print(" " * (2 * (baris - i)), end=" ")

    for j in range(i, 0, -1):
        print(j, end="")

    print()  
 