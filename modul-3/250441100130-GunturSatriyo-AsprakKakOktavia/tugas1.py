print("bil prima")
bilangan = int(input("masukkan bilangan : "))
for jumlah in range (2, bilangan + 1):
    prima = 0
    for i in range(1, jumlah + 1):
        if jumlah % i == 0:
            prima += 1
    if prima == 2:
        print("bil prim ", jumlah)
    
