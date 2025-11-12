print("Bilangan Prima sampai N")
n = int(input("Masukkan nilai N : "))
for jumlah in range(2, n + 1):
    prima = 0
    for i in range(1, jumlah + 1):
        if jumlah % i == 0:
            prima += 1
    if prima == 2:
        print("bilangan prima ", jumlah)