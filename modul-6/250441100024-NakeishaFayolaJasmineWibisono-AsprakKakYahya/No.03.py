data = []

def menu():
    print("=== PROGRAM CEK PEMBAGIAN ANGKA ===")
    print("1. Tambah angka")
    print("2. Tampilkan data")
    print("3. Rubah angka")
    print("4. Hapus angka")
    print("5. Cek apakah angka bisa dibagi dua bagian dengan jumlah yang sama")
    print("6. Keluar")

#fungsi menghitung jumlah
def hitung_jumlah(daftar):
    total = 0
    for angka in daftar:
        total += angka
    return total

#Cek apakah bisa dibagi dua bagian
def cek_bagian():
    if len(data) % 2 != 0:
        print("Jumlah data harus genep agar bisa dibagi dua.")
        return
    tengah = len(data) // 2
    bagian1 = data[:tengah]
    bagian2 = data[tengah:]

    total1 = hitung_jumlah(bagian1)
    total2 = hitung_jumlah(bagian2)

    print("Bagian 1: ", bagian1, "Jumlahnya: ", total1)
    print("Bagian 2: ", bagian2, "Jumlahnya: ", total2)

    if total1 == total2:
        print("Hasilnya benar (Jumlah kedua bagiannya sama)")
    else:
        print("Hasilnya salah (Jumlah kedua bagiannya tidak sama)")

#program utama
while True:
    menu()
    pilih = input("pilih menu (1-6): ")

    if pilih == "1":
        angka = int(input("Masukkan angka: "))
        data.append(angka)
    elif pilih == "2":
        print("Data saat ini adalah: ", data)
    elif pilih == "3":
        indeks = int(input("Rubah angka di posisi ke berapa? "))
        if 0<= indeks < len(data):
            baru = int(input("Masukkan angka baru: "))
            data[indeks] = baru
        else:
            print("Letaknya tidak valid!")
    elif pilih == "4":
        indeks = int(input("Hapus angka di posisi ke berapa? "))
        if 0 <= indeks < len(data):
            del data[indeks]
        else:
            print("posisinya tidak valid!")
    elif pilih == "5":
        cek_bagian()
    elif pilih == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi")