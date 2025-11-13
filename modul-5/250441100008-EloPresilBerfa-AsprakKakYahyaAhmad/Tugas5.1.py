def faktorial(n):
    if n == 0:
        return 1
    else:
        return n*faktorial(n-1)

n = int(input("Input Bilangan Non-Negatif : "))

if n < 0:
    print("Tidak Dapat Menghitung Bilangan Negatif.")
else:
    hasil = faktorial(n)
    print(f"Faktorial dari {n} adalah : {hasil}")