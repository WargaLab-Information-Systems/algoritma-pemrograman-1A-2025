def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

try:
    N = int(input("Masukkan bilangan bulat non-negatif (N): "))
    
    if N < 0:
        print("Maaf, faktorial tidak didefinisikan untuk bilangan negatif.")
    else:
        hasil = faktorial(N)
        print(f"Faktorial dari {N} adalah: {hasil}")

except ValueError:
    print("Input tidak valid! Harap masukkan bilangan bulat.")