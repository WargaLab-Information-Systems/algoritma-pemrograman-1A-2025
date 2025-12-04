angka = []

def hitung_panjang(data):
    count = 0
    for x in data:  
        count += 1
    return count

def tambah():
    jumlah = int(input("Ingin menambahkan berapa angka? "))
    for i in range(jumlah):
        n = int(input(f"Masukkan angka ke-{i+1}: "))
        angka.append(n)
    print(f"{jumlah} angka berhasil ditambahkan!\n")

def tampil():
    print("Daftar angka:", angka, "\n")

def ubah():
    idx = int(input("Masukkan indeks yang ingin diubah: "))
    count = hitung_panjang(angka)
    if 0 <= idx < count:
        angka_baru = int(input("Masukkan angka baru: "))
        for i in range(count): 
            if i == idx:
                angka[i] = angka_baru
                print("Data berhasil diubah!\n")
                break
    else:
        print("Indeks tidak valid.\n")

def hapus():
    idx = int(input("Masukkan indeks yang ingin dihapus: "))
    count = hitung_panjang(angka)
    if 0 <= idx < count:
        for i in range(count):
            if i == idx:
                del angka [i]
        print("Data dihapus!\n")
    else:
        print("Indeks tidak valid.\n")

def cek_pembagian():
    total = 0
    for x in angka:  
        total += x
    if total % 2 != 0:
        print("False (jumlah total ganjil, tidak bisa dibagi dua sama besar)\n")
        return

    half = total // 2
    left_sum = 0
    for x in angka:
        left_sum += x
        if left_sum == half:
            print("True (bisa dibagi dua bagian dengan jumlah sama)\n")
            return
    print("False (tidak bisa dibagi dua sama besar)\n")

while True:
    print("=== PROGRAM PEMBAGIAN ANGKA = ==")
    print("1. Tambah Angka")
    print("2. Tampilkan Angka")
    print("3. Ubah Angka")
    print("4. Hapus Angka")
    print("5. Cek Pembagian")
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
        cek_pembagian()
    elif pilih == "6":
        print("program selesai.terima kasih")
        break
    else:
        print("Pilihan tidak valid!\n")