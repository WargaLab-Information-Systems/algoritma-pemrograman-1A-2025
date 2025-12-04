data = []

def tambah():
    angka = int(input("Masukkan angka yang ingin ditambahkan: "))
    data.append(angka)
    print("Angka berhasil ditambahkan.")

def tampil():
    print("Daftar angka saat ini:", data)

def ubah():
    tampil()
    index = int(input("Masukkan index angka yang ingin diubah: "))
    if 0 <= index < len(data):
        angka_baru = int(input("Masukkan nilai baru: "))
        data[index] = angka_baru
        print("Data berhasil diubah.")
    else:
        print("Index tidak valid!")

def hapus():
    tampil()
    index = int(input("Masukkan index angka yang ingin dihapus: "))
    if 0 <= index < len(data):
        del data[index]
        print("Data berhasil dihapus.")
    else:
        print("Index tidak valid!")

def cek_pembagian():
    if len(data) % 2 != 0:
        print("False (Jumlah elemen ganjil, tidak bisa dibagi dua sama panjang)")
        return
    
    tengah = len(data) // 2
    bagian1 = data[:tengah]
    bagian2 = data[tengah:]
    
    total1 = 0
    for x in bagian1:
        total1 += x
    
    total2 = 0
    for y in bagian2:
        total2 += y
    
    if total1 == total2:
        print("True (Jumlah kedua bagian sama)")
    else:
        print("False (Jumlah kedua bagian berbeda)")

while True:
    print("\n=== MENU ===")
    print("1. Tambah Angka")
    print("2. Tampilkan Angka")
    print("3. Ubah Angka")
    print("4. Hapus Angka")
    print("5. Cek Pembagian Deret")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampil()
    elif pilihan == "3":
        ubah()
    elif pilihan == "4":
        hapus()
    elif pilihan == "5":
        cek_pembagian()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")