# Program kondisi lampu di taman kota

# Meminta input jumlah baris lampu
jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

# Perulangan untuk setiap baris lampu
for y in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris {y}: "))
    
    # Perulangan untuk setiap lampu di baris tersebut
    for x in range(1, jumlah_lampu + 1):
        if x % 3 == 0:  # Jika nomor lampu kelipatan 3
            print(f"Lampu ke-{x} pada baris {y} rusak.")
        else:
            print(f"Lampu ke-{x} pada baris {y} menyala.")
    
    # Jika baris terakhir, tambahkan pesan tambahan
    if y == jumlah_baris:
        print("Periksa sambungan daya utama.")
