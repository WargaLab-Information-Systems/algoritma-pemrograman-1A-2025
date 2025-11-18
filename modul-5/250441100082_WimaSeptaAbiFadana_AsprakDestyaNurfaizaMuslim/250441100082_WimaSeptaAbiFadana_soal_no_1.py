def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

n = int(input("masukan bilangan bulat : "))

if n < 0:
    print("angka harus positif!")
else:
    print("faktorial dari", n, "adalah", faktorial(n))