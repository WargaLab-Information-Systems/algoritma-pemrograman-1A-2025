# Program menghitung faktorial secara rekursif

def faktorial(n):
   
    # Basis rekurensinya, jika n == 0 atau 1 maka hasilnya 1
    if n == 0 or n == 1:
        return 1
    else:
        # Pemanggilan fungsi secara rekursif
        return n * faktorial(n - 1)


# Bagian utama program (dinamis)
try:
    angka = int(input("Masukkan bilangan bulat non-negatif: "))
    if angka < 0:
        print("Bilangan harus non-negatif!")
    else:
        hasil = faktorial(angka)
        print(f"Hasil faktorial dari {angka}! adalah {hasil}")
except ValueError:
    print("Input harus berupa angka bulat!")
