def faktorial(n):
    if n == 0 or n == 1: 
        n = 1
        return n
    else:  
        return n * faktorial(n - 1)

angka = int(input("Masukkan bilangan bulat :"))
if angka < 0:
    print("Input tidak boleh negatif")
else:
    print(f"Faktorial dari {angka} adalah: {faktorial(angka)}")