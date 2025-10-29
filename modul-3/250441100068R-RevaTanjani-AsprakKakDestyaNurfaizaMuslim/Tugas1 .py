n = int(input("masukkan sampai berapa batas bilangan?"))
for i in range(2,n + 1, 1):
    faktor = 0
    for h in range(1,i+1, 1):
        if i % h == 0:
            faktor = faktor + 1
    if faktor == 2:
            print(i)