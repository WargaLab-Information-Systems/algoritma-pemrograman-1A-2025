angka = []

def tambah():
    x = int(input("Masukkan angka: "))
    angka.append(x)

def ubah():
    i = int(input("Index yang mau diubah: "))
    if 0 <= i < len(angka):
        angka[i] = int(input("Angka baru: "))
    else:
        print("Index tidak valid!")

def hapus():
    i = int(input("Index yang mau dihapus: "))
    if 0 <= i < len(angka):
        angka.pop(i)
    else:
        print("Index tidak valid!")

def tampil():
    print("Data:", angka)

def cek_bagi_dua():
    total = sum(angka)
    if total % 2 != 0:
        print(False)
        return
    target = total // 2
    temp = 0
    for i in range(len(angka)):
        temp += angka[i]
        if temp == target:
            print(True)
            return
    print(False)

while True:
    print("\n1. Tambah\n2. Ubah\n3. Hapus\n4. Tampil\n5. Cek Bagi Dua\n6. Keluar")
    pilih = input("Pilih: ")
    if pilih == "1":
        tambah()
    elif pilih == "2":
        ubah()
    elif pilih == "3":
        hapus()
    elif pilih == "4":
        tampil()
    elif pilih == "5":
        cek_bagi_dua()
    elif pilih == "6":
        break
    else:
        print("Pilihan salah!")