#N0 1
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1) 

# Program utama
angka = int(input("Masukkan bilangan bulat non-negatif: "))
hasil = faktorial(angka)
print(f"Faktorial dari {angka} adalah {hasil}")

def rika():
    print("haklo")

rika()