baris_lampu = int(input("Masukkan jumlah baris lampu : "))

for i in range(1, baris_lampu + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris ke-{i}: "))

    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 != 0:
            print("Lampu ke - ", lampu, "pada baris ke - ", i , "menyala")
        else:
            print("Lampu ke - ", lampu, "pada baris ke - ", i , "rusak")
    
    if i == baris_lampu:
        print("Periksa sambungan daya utama.")
    print()
