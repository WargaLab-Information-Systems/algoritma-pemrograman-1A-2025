# Program menampilkan kondisi lampu taman kota
#jika genap terang
#jika ganjil redup
#jika kelipatan 5
n = int(input("Jumlah baris lampu: "))
jumlah_lampu = 1
for baris in range(1, n + 1):
    jumlah = int(input(f"Jumlah lampu baris {baris}: "))
    for lampu in range(jumlah): 
        if jumlah_lampu % 5 == 1:
            print(f"Lampu ke-{jumlah_lampu} pada baris {baris} berkedip cepat.")
        elif jumlah_lampu % 2 == 0:
            print(f"Lampu ke-{jumlah_lampu} pada baris {baris} terang")
        else:
            print(f"lampu ke-{jumlah_lampu} pada baris {baris} redup")
    
        jumlah_lampu += 1
    if baris == n:
        print("Periksa sambungan daya utama.")