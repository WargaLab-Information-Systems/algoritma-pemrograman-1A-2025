# Meminta input dari pengguna
n = int(input("Masukkan nilai n: "))
# Loop untuk setiap baris
for i in range(1, n + 1):
    for j in range(1, i + 1): # Sisi kiri piramida
        print(j, end="")
    spasi = (n - i) * 2     # Spasi di tengah
    for k in range(spasi):
        print(" ", end="")
    for l in range(i, 0, -1):# Sisi kanan piramida (cermin)
        print(l, end="")
            # Pindah ke baris berikutnya
    print()
