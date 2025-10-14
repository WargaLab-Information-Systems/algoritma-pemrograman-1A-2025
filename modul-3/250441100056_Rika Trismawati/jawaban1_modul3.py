# menampilan bilangan prima dai 1 sampai n

percobaan = 1
while percobaan <= 1:
    n = int(input("masukkan batas bilangan"))
    print(f"jadi bilangan 1 sampai {n} prima adalah")
    for i in range(2, n + 1):
        prima = True
        for j in range(2, i):
            if i % j == 0:
                prima = False
        if prima :
            print(i, end=" ")
    percobaan += 1
    

    
     



         