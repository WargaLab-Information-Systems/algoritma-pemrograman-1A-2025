angka = []  # List utama untuk menyimpan data

def tambah_data():
    n = int(input("Masukkan angka yang ingin ditambah: "))
    angka.append(n)
    print("Angka berhasil ditambahkan!")

def tampil_data():
    if len(angka) == 0:
        print("Belum ada data.")
    else:
        print("Daftar angka:", angka)

def ubah_data():
    tampil_data()
    if len(angka) == 0:
        return
    index = int(input("Masukkan indeks data yang ingin diubah (mulai dari 0): "))
    if 0 <= index < len(angka):
        baru = int(input("Masukkan nilai baru: "))
        angka[index] = baru
        print("Data berhasil diubah!")
    else:
        print("Indeks tidak valid!")

def hapus_data():
    tampil_data()
    if len(angka) == 0:
        return
    index = int(input("Masukkan indeks data yang ingin dihapus (mulai dari 0): "))
    if 0 <= index < len(angka):
        del angka[index]
        print("Data berhasil dihapus!")
    else:
        print("Indeks tidak valid!")

def cek_dua_bagian():
    if len(angka) < 2:
        print("Data terlalu sedikit untuk dibagi dua.")
        return

    total = 0
    for a in angka:
        total += a

    if total % 2 != 0:
        print("Total ganjil, tidak bisa dibagi dua sama besar.")
        print("Hasil: False")
        return

    tengah = total // 2
    jumlah_kiri = 0

    for a in angka:
        jumlah_kiri += a
        if jumlah_kiri == tengah:
            print("Bisa dibagi menjadi dua bagian dengan jumlah sama.")
            print("Hasil: True")
            return

    print("Tidak bisa dibagi menjadi dua bagian dengan jumlah sama.")
    print("Hasil: False")

# ===== Menu Utama =====
while True:
    print("\n===== PROGRAM DERETAN ANGKA DOMINIC =====")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cek Dua Bagian Sama")
    print("6. Keluar")

    menu = input("Pilih menu (1-6): ")

    if menu == "1":
        tambah_data()
    elif menu == "2":
        tampil_data()
    elif menu == "3":
        ubah_data()

    elif menu == "4":
        hapus_data()
    elif menu == "5":
        cek_dua_bagian()
    elif menu == "6":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Menu tidak valid!")

