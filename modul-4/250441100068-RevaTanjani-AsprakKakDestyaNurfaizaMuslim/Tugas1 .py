jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
for baris in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris {baris}: "))
    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"Lampu ke-{lampu} di baris {baris} rusak")
        else:
            print(f"Lampu ke-{lampu} di baris {baris} menyala") 
print("Semua baris telah diperiksa. Periksa sambungan daya utama jika ada masalah.")