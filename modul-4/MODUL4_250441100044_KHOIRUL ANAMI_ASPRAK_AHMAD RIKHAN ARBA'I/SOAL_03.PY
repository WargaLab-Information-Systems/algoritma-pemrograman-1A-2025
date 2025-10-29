# SOAL NO 3
X = str("SOAL NO 3")
print(X)

n = int(input("Silahkan maukkan angka  n untuk membuat piramida: "))

for i in range (n, 0, -1):

    for baris_kiri in range (1, i + 1):
        print (f"{baris_kiri:3}", end="")

    spasi = (n - i) * 6
    print (" " * spasi, end="")

    for baris_kanan in range (i, 0, -1):
        print(f"{baris_kanan:3}", end="")
        
    print ()

print("\nini dia hasil piramida yang kamu inginkan😊😊😁")