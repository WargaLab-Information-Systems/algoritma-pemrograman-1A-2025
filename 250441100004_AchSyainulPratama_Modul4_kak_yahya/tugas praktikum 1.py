baris = int(input("Masukkan jumlah baris lampu: "))

for y in range(1, baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris ke-{y}: "))
    print(f"\nKondisi lampu baris ke-{y}:")
    
    lampu = ["menyala", "menyala", "rusak"]
    index = 0
    
    for x in range(1, jumlah_lampu + 1):
        print(f"Lampu ke-{x} pada baris [{y}] {lampu[index]}.")
        index += 1
        if index == len(lampu):
            index = 0

    print("Periksa sambungan daya utama.\n")