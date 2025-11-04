n = input("Masukkan nilai n: ")

# cek apakah input hanya angka
if not n.isdigit():
    print("Input harus berupa angka, bukan huruf atau simbol!")
else:
    # ubah ke integer
    n = int(n)
# cek nilai minimal
    if n < 2:
        print("Nilai n harus 2 atau lebih!")
    else:
        print(f"Bilangan prima (2 - {n}):")

        # perulangan dan kondisi pada bilangan prima
        for i in range(2, n + 1):     # mengecek semua angka dari 2-n
            for j in range(2, i):     # mengecek pembagi dari 2 sampai i-1
                if i % j == 0:        # jika ada pembagi selain 1 dan dirinya sendiri
                    break
            else:
                print(i)


