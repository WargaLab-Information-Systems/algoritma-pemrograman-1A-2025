# Program menghitung faktorial menggunakan fungsi rekursif

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

# Program utama
n = int(input("Masukkan bilangan bulat non-negatif: "))
if n < 0:
    print("Bilangan tidak boleh negatif!")
else:
    print(f"Faktorial dari {n} adalah {faktorial(n)}")
