print("="*10," Tugas 1 Modul 4 ","="*20)

J_baris = int(input("Masukkan Jumlah Baris Lampu "))

for baris in range (1,J_baris+1):
    j_lampu = int(input(f"Masukan Jumlah Lampu Pada Baris Ke -{baris}: "))
    for lampu in range (1,j_lampu+1):
        if lampu % 3 == 0:
            print(f" Lampu Ke-{lampu} Pada Baris {baris} Rusak.")
        else:
            print(f" Lampu Ke-{lampu} Pada Baris {baris} Menyala.")
    if baris == J_baris:
        print("Periksa Sambungan Daya Utama.\n")


 