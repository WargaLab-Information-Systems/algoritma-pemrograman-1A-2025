n = int(input("masukan maksimalnya : "))

for n in range(2,n + 1):
    prima = True

    for i in range(2,n):
        if n % i == 0:
            prima = False
            break

    if prima:
        print("jadi bilangan primanya : ", n)