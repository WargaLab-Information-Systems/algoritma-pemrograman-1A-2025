# Program mencetak dua piramida angka yang saling berhadapan

# Meminta input tinggi piramida
n = int(input("Masukkan tinggi piramida (n): "))

# Perulangan untuk setiap baris
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")

    spasi = (n - i) * 2
    for k in range(spasi):
        print(" ", end="")

    for j in range(i, 0,-1):
        print(j, end="")

    # Pindah ke baris berikutnya
    print()
