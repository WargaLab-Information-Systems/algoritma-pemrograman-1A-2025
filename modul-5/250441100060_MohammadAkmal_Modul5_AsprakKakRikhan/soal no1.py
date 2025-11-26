def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

angka = int(input("Masukkan angka untuk menghitung faktorial: "))
print("Hasil faktorial:", faktorial(angka))