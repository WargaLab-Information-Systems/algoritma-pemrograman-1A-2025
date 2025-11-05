n = int(input("Masukkan n :"))

for num in range(2, n + 1):
    prima = True
    for i in range (2, num):
        if num % i == 0:
            prima = False
            break
    if prima:
        print (num)