data_angka = []

def tambah_angka():
    angka = int(input("Masukkan angka baru: "))
    data_angka.append(angka)
    print("Angka berhasil ditambahkan.")

def tampilkan_angka():
    if len(data_angka) == 0:
        print("Belum ada data.")
        return
    else:
        print("Data saat ini:", data_angka)

def ubah_angka():
    tampilkan_angka()
    index = int(input("Masukkan indeks yang ingin diubah: "))
    if index >= 0 and index < len(data_angka):
        nilai_baru = int(input("Masukkan nilai baru: "))
        data_angka[index] = nilai_baru
        print("Data berhasil diubah.")
    else:
        print("Indeks tidak ditemukan.")
        return

def hapus_angka():
    tampilkan_angka()
    index = int(input("Masukkan indeks yang ingin dihapus: "))
    if index >= 0 and index < len(data_angka):
        del data_angka[index]
        print("Data berhasil dihapus.")
    else:
        print("Indeks tidak ditemukan.")
        return

def cek_keseimbangan():
    if len(data_angka) == 0:
        print("Tidak ada data untuk dicek.")
        return

    total = 0
    for angka in data_angka:
        total += angka

    if total % 2 != 0:
        print("False (jumlah total ganjil, tidak bisa dibagi dua sama besar)")
        return

    setengah = total // 2
    jumlah = 0
    for angka in data_angka:
        jumlah += angka
        if jumlah == setengah:
            print("True (bisa dibagi dua bagian sama besar)")
            return

    print("False (tidak bisa dibagi dua bagian sama besar)")

while True:
    print("\n=== PROGRAM CRUD ===")
    print("1. Tambah Angka")
    print("2. Tampilkan Angka")
    print("3. Ubah Angka")
    print("4. Hapus Angka")
    print("5. Cek Keseimbangan")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_angka()
    elif pilihan == "2":
        tampilkan_angka()
    elif pilihan == "3":
        ubah_angka()
    elif pilihan == "4":
        hapus_angka()
    elif pilihan == "5":
        cek_keseimbangan()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
