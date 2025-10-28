baris = int(input("masukan jumlah baris "))
for i in range(1, baris + 1):
    lampu = int(input(f"masukan jumlah lampu baris ke - {i} "))
    print("="*40)
    for k in range(1, lampu + 1):
        if k % 3 == 0:
            print(f"lampu ke - {k} pada baris ke - {i} rusak")
        else:
            print(f"lampu ke - {k} pada baris ke - {i} menyala")
    if i == baris:
        print("Periksa sambungan utama")
    print("="*40)  