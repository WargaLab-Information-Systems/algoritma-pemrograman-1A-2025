def faktorial (n):
    if n == 0 or n == 1 :
        return 1
    else:
        return n * faktorial(n-1)

n = int(input("Masukkan bilangan bulat positif: "))
if n < 0:
    print("Faktorial hanya untuk bilangan lebih dari 0")
else:
    hasil = faktorial(n)
    print(f"Faktorial dari {n} adalah: {hasil}")
    
