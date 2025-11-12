
def create(data):
    angka = int(input("Masukkan angka baru: "))
    data.append(angka)
    print("Data berhasil ditambahkan.")

def read(data):
    if data == []:
        print("Data masih kosong.")
    else:
        print("Daftar angka:", data)

def update(data):
    if data == []:
        print("Data kosong, tidak bisa diubah.")
        return
    read(data)
    indeks = int(input("Masukkan indeks data yang ingin diubah: "))
    if 0 <= indeks < len(data):
        nilai_baru = int(input("Masukkan nilai baru: "))
        data[indeks] = nilai_baru
        print("Data berhasil diubah.")
    else:
        print("Indeks tidak valid.")

def delete(data):
    if data == []:
        print("Data kosong, tidak bisa dihapus.")
        return
    read(data)
    indeks = int(input("Masukkan indeks data yang ingin dihapus: "))
    if 0 <= indeks < len(data):
        del data[indeks]
        print("Data berhasil dihapus.")
    else:
        print("Indeks tidak valid.")

def cek_pembagian(data):
    total = 0
    for angka in data:
        total += angka

    if total % 2 != 0:
        return False

    target = total // 2
    jumlah_sementara = [False] * (target + 1)
    jumlah_sementara[0] = True

    for angka in data:
        for j in range(target, angka - 1, -1):
            if jumlah_sementara[j - angka]:
                jumlah_sementara[j] = True

    return jumlah_sementara[target]


def main():
    data = []
    while True:
        print("=== PROGRAM CRUD PEMBAGI ANGKA ===")
        print("1. Tambah data")
        print("2. Tampilkan data")
        print("3. Ubah data")
        print("4. Hapus data")
        print("5. Cek pembagian angka")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            create(data)
        elif pilihan == "2":
            read(data)
        elif pilihan == "3":
            update(data)
        elif pilihan == "4":
            delete(data)
        elif pilihan == "5":
            if data == []:
                print("Data kosong, tambahkan angka terlebih dahulu.")
            else:
                hasil = cek_pembagian(data)
                print("Hasil pemeriksaan:", hasil)
        elif pilihan == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
main()
