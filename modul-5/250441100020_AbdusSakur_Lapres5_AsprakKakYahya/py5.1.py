def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)
    
while True:
    try:
        n = int(input("masukkan biangan bulat non-negatif: "))
        if n < 0:
            print("bilangan tidak boleh negatif, coba lagi")
            continue
        break
    except ValueError:
        print("input tidak valid, coba lagi")

hasil = faktorial(n)  
print(f"faktorial dari {n} adalah {hasil}")