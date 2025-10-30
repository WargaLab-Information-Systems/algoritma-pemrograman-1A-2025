baris = int(input("Masukkan jumlah baris lampu: "))

for i in range(1, baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris {i}: "))
    for j in range(1, jumlah_lampu + 1):
        if j % 3 == 0:
            print(f"Lampu ke-{j} pada baris {i} rusak.", end=" ")
        else:
            print(f"Lampu ke-{j} pada baris {i} menyala.", end=" ")

        if i == baris:
            print("Periksa sambungan daya utama.")
        else:
            print()
