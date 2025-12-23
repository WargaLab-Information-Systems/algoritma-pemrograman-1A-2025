angka = []

def tambah():
    angka.append(int(input("masukkan angka : ")))

def tampil():
    print("angka sekarang : ", angka)

def ubah():
    index = int(input("indeks yang ingin diubah : "))
    if 0 <= index <len(angka):
        angka[index] = int(input("masukkan nilai baru : "))
    else:
        print("indeks tidak valid!")

def hapus():
    index = int(input("indeks yang ingin di hapus : "))
    if 0 <= index < len(angka):
        angka.pop(index)
    else:
        print("indeks tidak valid!")

def cek_apakah_bisa_dibagi():
    total = 0
    for x in angka:
        total += x
    if total % 2 != 0:
        print("false (totalnya ganjil)")
        return

    target = total // 2
    jumlah = 0
    bagian_kiri = []

    for x in angka:
        jumlah += x
        bagian_kiri.append(x)
        if jumlah == target:
            bagian_kanan = angka[len(bagian_kiri):]
            print("true (dapat dibagi menjadi dua bagian sama besar)")
            print("bagian kiri : ", bagian_kiri)
            print("bagian kanan : ", bagian_kanan)
            print("jumlah kedua bagiannya adalah : ", target, "dan", target)
            return
        if jumlah > target:
            break
    print("false (tidak dapat dibagi menjadi dua sama besar)")

while True:
    print("-----menu-----")
    print("1. tambah angka")
    print("2. tampilkan angka")
    print("3. ubah angka")
    print("4. hapus angka")
    print("5. cek apakah bisa dibagi menjadi dua")

    pilih = input("pilih menu : ")

    if pilih == "1":
        tambah()
    elif pilih == "2":
        tampil()
    elif pilih == "3":
        ubah()
    elif pilih == "4":
        hapus()
    elif pilih == "5":
        cek_apakah_bisa_dibagi()
    else:
        print("pilihan tidak valid!")