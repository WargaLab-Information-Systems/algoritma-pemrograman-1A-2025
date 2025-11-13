print("="*10," Tugas 3 Modul 4 ","="*20)

n = int(input("Masukkan angka n : ")) #jumlah baris
for i in range(n,0,-1): # i nomer baris
    for j in range(1,i+1): # bagian kiri
        print(j, end=" ")

    for spasi in range ((n-i)*2): # bagian Tengah
        print(" ", end=" ")
        
    for k in range (i,0,-1): # bagian Kanan
        print(k, end=" ")

    print()
