angka_list = []

def tambah_angka():
    print("\n=== TAMBAH ANGKA ===")
    try:
        angka = int(input("Masukkan angka yang ingin ditambahkan: "))
        angka_list.append(angka)
        print("Angka berhasil ditambahkan.\n")
    except ValueError:
        print("Input harus berupa bilangan bulat!\n")

def tampilkan_angka():
    print("\n=== DAFTAR ANGKA ===")
    if not angka_list:
        print("List masih kosong.\n")
    else:
        for i, nilai in enumerate(angka_list):
            print(f"Index {i} : {nilai}")
        print()

def ubah_angka():
    print("\n=== UBAH ANGKA ===")
    if not angka_list:
        print("List masih kosong, tidak bisa mengubah.\n")
        return

    try:
        i = int(input("Masukkan index angka yang ingin diubah: "))
        if i < 0 or i >= len(angka_list):
            print("Index tidak valid!\n")
            return

        nilai_baru = int(input("Masukkan nilai baru: "))
        angka_list[i] = nilai_baru
        print("Data berhasil diubah.\n")

    except ValueError:
        print("Input harus berupa angka!\n")

def hapus_angka():
    print("\n=== HAPUS ANGKA ===")
    if not angka_list:
        print("List masih kosong, tidak bisa menghapus.\n")
        return

    try:
        i = int(input("Masukkan index angka yang ingin dihapus: "))
        if i < 0 or i >= len(angka_list):
            print("Index tidak valid!\n")
            return

        angka_list.pop(i)
        print("Data berhasil dihapus.\n")

    except ValueError:
        print("Input harus berupa angka!\n")

def cek_pembagian():
    print("\n=== CEK PEMBAGIAN LIST ===")

    if not angka_list:
        print("List masih kosong, tidak bisa dicek.\n")
        return

    total = 0

    for x in angka_list:
        total += x
    if total % 2 == 1:
        print("False (Jumlah total ganjil, tidak dapat dibagi dua sama besar)\n")
        return

    target = total // 2
    kiri = 0
    for item in angka_list:
        kiri += item
        if kiri == target:
            print("True (List dapat dibagi menjadi dua bagian dengan jumlah sama)\n")
            return
        elif kiri > target:
            break

    print("False (Tidak ada titik pembagi yang sesuai)\n")

while True:
    print("===================================================")
    print("      PROGRAM LIST ANGKA DOMINIC SZOBOSZLAI")
    print("===================================================")
    print("1. Tambah Angka (Create)")
    print("2. Tampilkan Angka (Read)")
    print("3. Ubah Angka (Update)")
    print("4. Hapus Angka (Delete)")
    print("5. Cek Pembagian Dua Bagian")
    print("6. Keluar")
    print("---------------------------------------------------")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tambah_angka()
    elif pilihan == "2":
        tampilkan_angka()
    elif pilihan == "3":
        ubah_angka()
    elif pilihan == "4":
        hapus_angka()
    elif pilihan == "5":
        cek_pembagian()
    elif pilihan == "6":
        print("\nProgram selesai. Terima kasih.\n")
        break
    else:
        print("Pilihan tidak valid!\n")
