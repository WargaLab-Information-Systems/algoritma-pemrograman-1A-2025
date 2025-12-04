n = int(input("Masukkan Baris Lampu :"))

for i in range(1,n+1):
    j = int(input(f"Masukkan Jumlah Lampu/baris ke-{i} :"))
    
    for k in range(1,j+1):
        if k % 3 == 0:
            print(f"Lampu ke-{k} Pada Baris {i} Rusak.")
        else:
            print(f"Lampu ke-{k} Pada Baris {i} Menyala.")
            
    if i == n:
        print("Periksa sambungan daya utama.")
