print("="*15," Tugas 1 Bilangan Prima ","="*15)

#inputan Batas Akhir
n = int(input('Masukkan Nilai N : '))

print(f"Bilangan Prima Dari 1 - {n} Adalah : ")

# Perulangan Dari 2 Sampai n
for j in range(2,n + 1):
    Prima = True # J di Anggap Bilangan Prima

    # Cek Apakah J Memiliki Pembagi Selain 1 Dan Dirinya sendiri
    for k in range(2, int(j**0.5) +1):
        if j % k == 0 :
            Prima = False
            break
    #jika Prima Masih True Maka j adalah Prima
    if Prima:
        print(j, end=" ") # End Untuk Menambah sepasi Dari print




#Biasakan Mengerjakan Soal cerita untuk latihan 

# for i in range(2,10,2):
#     print(i)

# while True:
#     print ("aku")