def faktorial(n):
    if n == 0 or n == 1 :
        return 1
    else :
        return n * faktorial(n - 1)
    

while True:
    try :
        n = int(input("Masukkan bilangan bulat non negatif : "))
        if n < 0 :
            print("Input tidak boleh negatif!!")
        else :
            hasil = faktorial(n)
            print(f"Hasil : {n} != {hasil}")
            break
    except ValueError:
        print("Input harus berupa bilangan bulat non negatif, Masukkan lagi :")