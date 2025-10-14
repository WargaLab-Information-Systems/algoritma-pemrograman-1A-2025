# Input
n = int(input("Masukkan nilai n: "))

# Perulangan untuk mencari dan mencetak bilangan prima
for angka in range(2, n + 1):
    bilangan_prima = True
    # Cek faktor sampai akar kuadrat angka
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            bilangan_prima = False
            break
            
    # Output
    if bilangan_prima:
        print(angka, end=" ")