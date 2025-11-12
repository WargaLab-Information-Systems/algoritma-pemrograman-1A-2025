# Menghitung faktorial bersifat dinamis
def faktorial(N):
    return 1 if N <= 1 else N * faktorial(N - 1) # N dikalikan dengan hasil faktorial dari satu angka sebelumnya.
try:
    N = int(input("Masukkan bilangan bulat (bukan negatif): "))
    while N < 0:
        print("Tolong masukkan bilangan (bukan negatif!)")
        N = int(input("Masukkan bilangan bulat (bukan negatif): "))

    # Menampilkan hasil faktorial
    print(f"Faktorial dari {N} adalah: {faktorial(N)}")

except ValueError:
    print("Input tidak valid! Harap masukkan bilangan bulat.")