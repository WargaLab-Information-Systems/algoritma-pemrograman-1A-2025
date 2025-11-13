# Program Dominic Szoboszlai - CRUD dan Pembagian List

data = []

def tambah():
    nilai = int(input("Masukkan angka: "))
    data.append(nilai)

def tampil():
    print("Data saat ini:", data)

def ubah():
    idx = int(input("Masukkan indeks data yang ingin diubah: "))
    if 0 <= idx < len(data):
        nilai_baru = int(input("Masukkan nilai baru: "))
        data[idx] = nilai_baru
    else:
        print("Indeks tidak valid.")

def hapus():
    idx = int(input("Masukkan indeks data yang ingin dihapus: "))
    if 0 <= idx < len(data):
        del data[idx]
    else:
        print("Indeks tidak valid.")

def cek_pembagian_sama():
    total = sum(data)
    half = total / 2
    temp = 0
    for i in range(len(data)):
        temp += data[i]
        if temp == half:
            return True
    return False

def menu():
    while True:
        print("\n=== MENU DOMINIC ===")
        print("1. Tambah data")
        print("2. Tampilkan data")
        print("3. Ubah data")
        print("4. Hapus data")
        print("5. Cek pembagian sama")
        print("6. Keluar")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah()
        elif pilih == "2":
            tampil()
        elif pilih == "3":
            ubah()
        elif pilih == "4":
            hapus()
        elif pilih == "5":
            print("Hasil:", cek_pembagian_sama())
        elif pilih == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

menu()
