# Program menghitung faktorial secara rekursif
# Kasus: Pak Tungtung ingin membuka brankas tua yang membutuhkan perhitungan faktorial

def faktorial(n):
    # Basis rekursi: jika n = 0 atau n = 1, maka faktorialnya adalah 1
    if n == 0 or n == 1:
        return 1
    else:
        # Pemanggilan rekursif
        return n * faktorial(n - 1)

# Program utama (dinamis, menerima input dari pengguna)
try:
    N = int(input("Masukkan bilangan bulat non-negatif (N): "))
    
    if N < 0:
        print("Maaf, faktorial tidak didefinisikan untuk bilangan negatif.")
    else:
        hasil = faktorial(N)
        print(f"Faktorial dari {N} adalah: {hasil}")

except ValueError:
    print("Input tidak valid! Harap masukkan bilangan bulat.")
