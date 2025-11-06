print("="*50)
print("Nama : Elo Presil Berfa")
print("NIM : 250441100008")
print("="*50)

#Soal

#Dalam matematika, bilangan prima merupakan bilangan asli lebih besar dari 1 yang hanya memiliki dua faktor yaitu 1 dan bilangan itu sendiri. Buatkan program untuk menampilkan bilangan prima dari 1 sampai n.

#Jawaban

n = int(input("Masukkan nilai n : "))

for num in range(2, n + 1 ):
    prima = True
    for i in range(2, num):
        if num % i == 0:
            prima = False
            break
    if prima:
        print(num)


print("="*50)