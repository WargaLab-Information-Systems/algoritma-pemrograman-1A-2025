n = int(input("Masukkan jumlah baris lampu: "))

jumlah_lampu = 1

for y in range(1, n + 1):
    m = int(input(f"Masukkan jumlah lampu di baris {y}: "))
    
    for i in range(m):
        x = jumlah_lampu
        if x % 3 == 2:
            print(f"Lampu ke-{x} pada baris {y} rusak.")
        else:
            print(f"Lampu ke-{x} pada baris {y} menyala.")
        jumlah_lampu += 1
    if y == n:
        print("Periksa sambungan daya utama.")