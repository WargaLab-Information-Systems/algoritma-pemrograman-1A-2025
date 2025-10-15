while True:
    try:
        n = int(input("Masukkan nilai n : "))
        break  # keluar dari loop jika input valid (angka)
    except ValueError:
        print("Input harus berupa angka! Silakan coba lagi.\n")

print("Bilangan prima dari 1 sampai", n, "adalah :")
for i in range(2, n + 1):
    prima = True
    for j in range(2, i):
        if i % j == 0:
            prima = False
            break
    if prima:
        print(i, end=" ")
