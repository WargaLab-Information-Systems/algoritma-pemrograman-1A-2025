jumlah_baris = int(input("berapa jumlah baris lampu : "))

for i in range(1,jumlah_baris + 1):
    jumlah_lampu = int(input(f"berapa jumlah lampu pada baris ke {i} :"))
    
    rusak = False

    for j in range(1,jumlah_lampu + 1):
            if j % 3 == 0:
                print("lampu ke", j, "pada baris", i, "rusak")
                rusak = True
            else:
                print("lampu ke", j, "pada baris", i, "menyala")

    if i == jumlah_baris and rusak:
        print("periksa sambungan daya utama")