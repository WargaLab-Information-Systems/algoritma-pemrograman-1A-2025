#tuple awal
t1 = tuple(map(int, input("Masukkan elemen tuple 1: ").split()))
t2 = tuple(map(int, input("Masukkan elemen tuple 2: ").split()))
#1. menggabungkan tuple
gabung = t1 + t2
#2. menghapus angka duplikat (tetap urut)
angka_unik = []
for angka in gabung:
    if angka not in angka_unik:
        angka_unik.append(angka)
#3. Urutan menurun (descending)
#angka_unik.sort(reverse=True)
for i in range(len(angka_unik)):
    for j in range(len(angka_unik) - 1):
        if angka_unik[j] < angka_unik[j + 1]:
            #tukar posisi
            simpan = angka_unik[j]
            angka_unik[j] = angka_unik[j + 1]
            angka_unik [j + 1] = simpan
#4. ubah hasil akhir menjadi tuple
hasil = tuple(angka_unik)
#5. outputnyaa
print("Hasil akhirnya adalah: ", hasil)
