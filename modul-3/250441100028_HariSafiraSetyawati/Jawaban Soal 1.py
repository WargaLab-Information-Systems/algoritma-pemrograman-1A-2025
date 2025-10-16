n = int(input("Masukkan nilai n: "))

for num in range(2, n + 1):
    bilangan_prima = True
    for i in range(2,num):
        if num % i == 0:
            bilangan_prima = False
            break
    if bilangan_prima:
        print(num)
print("Ini adalah bilangan prima-Nya")