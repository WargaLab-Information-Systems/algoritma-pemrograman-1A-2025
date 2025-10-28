# Program menampilkan kondisi lampu taman kota
jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

# Loop untuk setiap baris
for baris in range(1, jumlah_baris + 1): #- artinya perulangan dimulai dari 1 sampai jumlah_baris
    # Input jumlah lampu di baris ini
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris {baris}: ")) #Untuk setiap baris,diminta memasukkan berapa lampu yang ada di baris.
    
    # Loop untuk setiap lampu di baris ini
    for lampu in range(1, jumlah_lampu + 1): #- lampu akan berjalan dari 1 sampai jumlah lampu di baris itu.
        if lampu % 3 == 0: #- lampu yang nomornya kelipatan 3 dianggap rusak.
            print(f"Lampu ke-{lampu} pada baris {baris} rusak.")
        else:
            print(f"Lampu ke-{lampu} pada baris {baris} menyala.") # jika tidak dianggap menyala
    
# Jika baris terakhir, tambahkan pesan khusus
    if baris == jumlah_baris:
        print("Periksa sambungan daya utama.")