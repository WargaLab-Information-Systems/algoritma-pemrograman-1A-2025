data_angka = []

def create():
    n = int(input("Masukkan angka baru: "))
    data_angka.append(n)
    print("Angka berhasil ditambahkan!\n")
 
def read():
    if len(data_angka) == 0:
        print("Belum ada data.\n")
    else:
        print("Daftar angka saat ini:", data_angka, "\n")

def update():
    read()
    indeks = int(input("Masukkan indeks yang ingin diubah (mulai dari 0): "))
    if indeks < 0 or indeks >= len(data_angka):
        print("Indeks tidak valid!\n")
    else:
        nilai_baru = int(input("Masukkan nilai baru: "))
        data_angka[indeks] = nilai_baru
        print("Data berhasil diubah!\n")

def delete():
    read()
    indeks = int(input("Masukkan indeks yang ingin dihapus: "))
    if indeks < 0 or indeks >= len(data_angka):
        print("Indeks tidak valid!\n")
    else:
        del data_angka[indeks]
        print("Data berhasil dihapus!\n")

def cek_pembagian_sama():
    read()

    total = 0
    for i in data_angka:
        total += i

    if total % 2 != 0:
        print("Hasil: False (Jumlah total tidak bisa dibagi dua sama rata)\n")

    target = total // 2
    jumlah = 0

    for i in range(len(data_angka)):
        jumlah += data_angka[i]
        if jumlah == target:
            print("Hasil: True (Dapat dibagi menjadi dua bagian dengan jumlah sama)\n")
    print("Hasil: False (Tidak dapat dibagi menjadi dua bagian dengan jumlah sama)\n")

while True:
    print("1. Tambah Angka\n2. Lihat Angka\n3. Ubah Angka\n4. Hapus Angka\n5. Pembagian Sama\n6. Keluar")
    pilih = input("Pilih menu (1-6): ")

    if pilih == "1":
        create()
    elif pilih == "2":
        read()
    elif pilih == "3":
        update()
    elif pilih == "4":
        delete()
    elif pilih == "5":
        cek_pembagian_sama()
    elif pilih == "6":
        print("SeeYouu")
        break
    else:
        print("Pilihan tidak valid!\n")
