banyak = int(input("msukkan banyak deret "))
for i in range(0, banyak+1):
    if i > 1:
        faktor = 0
        for x in range(1, i+1):
            if i%x == 0:
                faktor += 1
        if faktor == 2:
            print(i)
  