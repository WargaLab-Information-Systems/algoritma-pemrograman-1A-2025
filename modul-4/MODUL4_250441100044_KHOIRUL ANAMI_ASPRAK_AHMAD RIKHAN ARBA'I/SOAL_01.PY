# SOAL NO 1
X = str("SOAL NO_1")
print (X)

jumlah_baris = int(input("Silahkan masukkan jumlah baris: "))

for i in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input("Silahkan masukkan jumlah lampu: "))
    for j in range (1, jumlah_lampu + 1) :
        if j % 3 == 0:
            print (f"lampu ke {j} pada baris ke {i} rusak😒 ")
        else :
            print(f"lampu ke {j} pada baris ke {i} menyala😁 ")

if i == jumlah_baris :
    print ("Periksa sambungan daya utama dan coba lagi ya...😊")

print ()




