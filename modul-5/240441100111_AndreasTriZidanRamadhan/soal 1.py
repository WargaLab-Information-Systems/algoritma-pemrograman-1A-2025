def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

N = int(input("Masukkan bilangan bulat: "))
if N < 0:
    print("Nilai harus non-negatif!")
else:
    hasil = faktorial(N)
    print(f"Faktorial dari {N} adalah {hasil}")
