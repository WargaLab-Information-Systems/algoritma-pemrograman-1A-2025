n = int(input("Masukan sampai beberapa batas bilangan?"))
for i in range (2,n + 1,1):
    prima = 0
    for kiki in range (1,i+1,1):
        if i % kiki == 0:
            prima = prima + 1
    if prima == 2:
        print(i)