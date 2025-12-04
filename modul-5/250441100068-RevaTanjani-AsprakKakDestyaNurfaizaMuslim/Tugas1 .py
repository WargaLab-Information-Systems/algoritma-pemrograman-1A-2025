def faktorial(n):
    print(n)
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)
n = int(input("Masukkan bilangan faktorial"))
if n < 0:
    print(f"{n}! = bukan bilangan faktorial")
else:
    print(f"{n}!=  ", faktorial(n))