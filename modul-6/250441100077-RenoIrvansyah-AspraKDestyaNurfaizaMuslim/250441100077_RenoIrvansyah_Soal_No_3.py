angka = []

def tambah():
    while True:
        input_angka = int(input("Masukkan angka: "))
        angka.append(input_angka)
        print("Angka berhasil ditambahkan!\n")

        lanjut = input("ingin lanjut isi angka? y/n : ")
        if lanjut == "y" :
            continue
        else:
            lanjut == "n"
            break

def lihat_data():
    print("Daftar angka:", angka, "\n")

def ubah_data_angka():
    lihat_data()
    
    print("list data angka : ")
    for i in range(len(angka)):
        print(f"Index {i} data {angka[i]}")

    if not angka:
        print("Tidak ada data untuk diubah!\n")
        return
    index_angka = int(input("Masukkan indeks yang ingin diubah (mulai dari 0): "))
    if 0 < index_angka < len(angka):
        nilai_baru = int(input("Masukkan angka baru: "))
        angka[index_angka] = nilai_baru
        print("Data berhasil diubah!\n")
    else:
        print("Indeks tidak valid!\n")

def hapus_data():

    lihat_data()

    print("list data angka : ")
    for i in range(len(angka)):
        print(f"Index {i} data {angka[i]}")
        
    if not angka:
        print("Tidak ada data untuk dihapus!\n")
        return
    index_angka = int(input("Masukkan indeks dari data yang ingin dihapus (mulai dari 0): "))
    if 0 <= index_angka < len(angka):
        angka.pop(index_angka)
        print("Data berhasil dihapus!\n")
    else:
        print("Indeks tidak valid!\n")

def cek_pembagian():
    
    if len(angka) % 2 != 0:
        print("Data tidak bisa dibagi dua bagian sama besar (jumlah elemen adalah ganjil)!\n")
        return
    tengah = len(angka) // 2
    kiri = angka[:tengah]
    kanan = angka[tengah:]
    print(f"Bagian kiri: {kiri} = {sum(kiri)}")
    print(f"Bagian kanan: {kanan} = {sum(kanan)}")
    print("Hasil:", sum(kiri) == sum(kanan), "\n")

def main():
    while True:
        print("="*50)
        print("1. Tambah Angka | 2. Lihat Angka | 3. Ubah Angka | 4. Hapus | 5. Cek Pembagian Sama Besar | 6. Keluar " )
        pilih = int(input("Pilih menu: "))

        if pilih == 1:
            tambah()
        elif pilih == 2:
            lihat_data()
        elif pilih == 3:
            ubah_data_angka()
        elif pilih == 4:
            hapus_data()
        elif pilih == 5:
            cek_pembagian()
        elif pilih == 6:
            print("Program selesai.")
            break
        else:
            print("Masukkan Pilihan yang benar!!\n")

main()
