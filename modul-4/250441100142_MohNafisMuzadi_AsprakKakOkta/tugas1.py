n = int(input("Masukkan Jumlah baris Lampu : "))
for i in range(1, n + 1):
    k = int(input(f"Masukkan jumlah lampu pada baris ke - {i} : "))
    for j in range(1, k + 1):
        if j % 3 != 0:
            print("Lampu ke -", j, "pada baris ke -", i, "menyala")
        else:
            print("Lampu ke -", j, "pada baris ke -", i, "rusak")
    if i == n:
        print("Periksa sambungan daya utama")
        
        