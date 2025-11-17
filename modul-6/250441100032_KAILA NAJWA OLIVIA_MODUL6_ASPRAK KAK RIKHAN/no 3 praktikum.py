# Program Deret Angka Dominic Szoboszlai
angka = []

def cek_sama(daftar):
    total = sum(daftar)
    if total % 2 != 0:
        return False
    setengah = total // 2
    jumlah = 0
    for i in daftar:
        jumlah += i
        if jumlah == setengah:
            return True
    return False

while True:
    print("\n=== PROGRAM CEK PEMBAGIAN ANGKA ===")
    print("1. Tambah Angka")
    print("2. Tampilkan Angka")
    print("3. Ubah Angka")
    print("4. Hapus Angka")
    print("5. Cek Pembagian Sama")
    print("6. Keluar")

    pilih = input("Pilih (1-6): ")

    if pilih == "1":
        angka_baru = int(input("Masukkan angka: "))
        angka.append(angka_baru)

    elif pilih == "2":
        print("Daftar angka:", angka)

    elif pilih == "3":
        if angka:
            i = int(input("Masukkan indeks angka yang ingin diubah: "))
            if 0 <= i < len(angka):
                angka[i] = int(input("Masukkan angka baru: "))
        else:
            print("Belum ada data.")

    elif pilih == "4":
        if angka:
            i = int(input("Masukkan indeks angka yang ingin dihapus: "))
            if 0 <= i < len(angka):
                angka.pop(i)
        else:
            print("Belum ada data.")

    elif pilih == "5":
        if angka:
            print("Hasil:", cek_sama(angka))
        else:
            print("Belum ada angka untuk dicek.")

    elif pilih == "6":
        print("Selesai.")
        break

    else:
        print("Pilihan salah.")
