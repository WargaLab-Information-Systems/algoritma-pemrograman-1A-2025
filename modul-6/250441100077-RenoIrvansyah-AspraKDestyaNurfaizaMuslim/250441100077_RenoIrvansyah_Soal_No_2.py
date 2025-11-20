t1 = tuple(map(int, input("masukkan beberapa angka : | pisahkan dengan spasi : ").split()))
t2 = tuple(map(int, input("masukkan beberapa angka : | pisahkan dengan spasi : ").split()))

hasil = tuple(set(t1 + t2))

print(f"ini adalah nilai asli setelah digabung : {hasil}")
for i in range(len(hasil)):
    for j in range(i + 1, len(hasil)):
        if hasil[i] < hasil[j]:
            simpan = list(hasil)
            simpan[i], simpan[j] = simpan[j], simpan[i]
            hasil = tuple(simpan)

print(f"Nilai setelah di sortir dari angka besar ke kecil{hasil}")