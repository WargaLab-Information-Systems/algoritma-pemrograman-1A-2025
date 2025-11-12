n = int(input("Masukkan jumlah baris lampu: "))

for y in range(1, n + 1):
    lampu = int(input(f"Masukkan jumlah lampu pada baris {y}: "))
    for x in range (1, lampu + 1):
        if x % 3 == 0:
            print(f"Lampu ke-{x} pada baris ({y}) rusak.")
        else:
            print(f"Lampu ke-{x} pada baris ({y}) menyala. ")
    if y == n:
        print("Periksa sambungan utama.")