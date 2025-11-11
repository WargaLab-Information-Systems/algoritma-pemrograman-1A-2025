# Mengecek kondisi lampu di taman kota
jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

for baris in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu di baris {baris}: "))
    for lampu in range(1, jumlah_lampu + 1):
        while lampu % 3 == 0:
            print(f"Lampu ke-{lampu} pada baris {baris} rusak.")
            break
        while lampu % 3 != 0:
            print(f"Lampu ke-{lampu} pada baris {baris} menyala.")
            break
    while baris == jumlah_baris:
        print("Periksa sambungan daya utama.") 
        break