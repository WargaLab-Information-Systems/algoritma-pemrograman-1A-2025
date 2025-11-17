data = []

def cek_pembagian_sama(data):
    total = 0
    for i in data:
        total += i
    jumlah_kiri = 0
    for i in range(len(data)):
        jumlah_kiri += data[i]
        jumlah_kanan = total - jumlah_kiri

        if jumlah_kiri == jumlah_kanan:
            return True
        
    return False

def tambah():
    banyak = int(input("Masukkan banyak nilai yang ingin dimasukkan: "))
    for i in range(banyak):
        nilai = int(input(f"Masukkan nilai ke-{i+1}: "))
        data.append(nilai)
    print("Data berhasil ditambahkan!")

def update():
    index = int(input("Masukkan index nilai yang ingin diubah: "))
    if 0 <= index < len(data):
        nilai_baru = int(input("Masukkan nilai baru: "))
        data[index] = nilai_baru
        print("Nilai berhasil diubah!")
    else:
        print("Index tidak valid!")

def hapus():
    nilai = int(input("Masukkan nilai yang ingin dihapus: "))
    if nilai in data:
        data.remove(nilai)
        print("Nilai berhasil dihapus!")
    else:
        print("Nilai tidak ditemukan!")

def tampilkan():
    if data:
        print("Isi list saat ini:", data)
    else:
        print("List masih kosong.")


while True:
    print("\n" + "- "*5, "MENU", "- "*5)
    print("1. BUAT LIST")
    print("2. UPDATE NILAI PADA LIST")
    print("3. HAPUS NILAI PADA LIST")
    print("4. CEK APAKAH LIST DAPAT DIBAGI 2 BAGIAN SAMA")
    print("5. LIHAT NILAI LIST")
    print("6. EXIT\n")

    masukan = int(input("Masukkan nomor menu: "))

    if masukan == 1:
        tambah()
    elif masukan == 2:
        update()
    elif masukan == 3:
        hapus()
    elif masukan == 4:
        print(cek_pembagian_sama(data))
    elif masukan == 5:
        tampilkan()
    elif masukan == 6:
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Nomor tidak sesuai.")
 