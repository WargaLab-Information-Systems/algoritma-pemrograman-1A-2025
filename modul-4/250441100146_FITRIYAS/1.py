# Program 1: Kondisi Lampu di Taman Kota

# Input jumlah baris lampu
baris = int(input("Masukkan jumlah baris lampu: "))

for y in range(1, baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris ke-{y}: "))
    for x in range(1, jumlah_lampu + 1):
        # Cek apakah lampu rusak (kelipatan 3)
        if x % 3 == 0:
            print(f"Lampu ke-{x} pada baris {y} rusak.")
        else:
            print(f"Lampu ke-{x} pada baris {y} menyala.")
    
print("Periksa sambungan daya utama.\n")
