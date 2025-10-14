#soal no 1 praktikum 09okt2025

n = int(input("Masukkan nilai n: "))
print("Bilangan Prima dari nilai n: ", end=" ")
for i in range(2, n+1):
    for a in range(2, i):
        if i % a == 0:
            break
    else:
        print(i, end=" ")

