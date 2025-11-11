def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
kunci = int(input("Masukkan bilangan non-negatif: "))
if kunci < 0:
    print("Masukkan bilangan non-negatif!")
else:
    hasil = fact(kunci)
    print(f"Faktorial dari {kunci} adalah {hasil}")


