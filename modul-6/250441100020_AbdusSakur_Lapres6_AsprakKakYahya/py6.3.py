angka = []

def tambah():
    try:
        x = int(input("Masukkan angka: "))
        angka.append(x)
    except:
        print("Masukkan angka yang valid.")

def tampil():
    print("Data angka:", angka)

def ubah():
    try:
        idx = int(input("Index yang diubah: "))
        baru = int(input("Nilai baru: "))
        angka[idx] = baru
    except:
        print("Index tidak valid.")

def hapus():
    try:
        idx = int(input("Index yang dihapus: "))
        angka.pop(idx)
        
    except:
        print("Index tidak valid.")

def cek_pembagian():
    total = 0
    for x in angka:
        total += x

    if total % 2 != 0:
        print(False)
        return

    setengah = total // 2

    sumi = 0
    for x in angka:
        sumi += x
        if sumi == setengah:
            print(True)
            return

    print(False)

while True:
    print("1. Tambah angka")
    print("2. Tampilkan angka")
    print("3. Ubah angka")
    print("4. Hapus angka")
    print("5. Cek apakah bisa dibagi")
    print("6. Keluar")

    p = input("Pilih menu: ")

    if p == "1":
        tambah()
    elif p == "2":
        tampil()
    elif p == "3":
        ubah()
    elif p == "4":
        hapus()
    elif p == "5":
        cek_pembagian()
    elif p == "6":
        break
    else:
        print("Pilihan tidak valid.")