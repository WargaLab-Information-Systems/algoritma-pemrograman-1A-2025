# no 1
def faktorial(N):
    if N == 0:
        return 1
    else:
        return N * faktorial(N - 1)
N = int(input("Masukkan bilangan bulat N: "))
if N < 0:
    print("Faktorial hanya untuk bilangan lebih dari 0.")
else:
    hasil = faktorial(N)
    print(f"Faktorial dari {N} adalah {hasil}")