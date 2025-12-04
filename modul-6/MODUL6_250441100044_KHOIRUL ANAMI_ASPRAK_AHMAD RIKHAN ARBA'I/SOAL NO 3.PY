X = ("SOAL NO 3")
print(X)


print("--PROGRAM CETAK DERET ANGKA DOMINIC--")

angka_list = []

while True:
    print("--MACAM MACAM PILIHAN--")
    print("1. Tambah Angka")
    print("2. Tampilkan semua angka")
    print("3. Ubah angka")
    print("4. Hapus angka")
    print("5. Cek apakah bisa dibagi dua bagian dengan jumlah sama")
    print("6. Keluar")

    pilihanmu = input("Silahakan masukkan pilihannmu (1-6): ")

    if pilihanmu == "1":

        angka = int(input("Silahkan masukkan nagka yang ingin ditmbahkan: "))
        angka_list.append(angka)


    elif pilihanmu == "2":
        if len(angka_list) == 0 :
            print ("Maaf belum ada list sama sekali")
        else :
            print("Daftar angka saat ini: ", angka_list)

    elif pilihanmu == "3":
        if len(angka_list) == 0:
            print("Maaf belum ada data untuk diubah ya")

        else: 
            print("Daftar angka sekarang", angka_list)
            update = int(input("Siahakan masukkan angka yang ingin diubah mulai dari index (0): "))
            if 0 <= update < len(angka_list):
                angka_baru = int(input("Silahakan masukkan angka baru:"))    
                angka_list[update] = angka_baru
                print ("Selamat data anda berhasil diubah")

            else:
                print ("Maaf data anda tidak ditemukan")


    elif pilihanmu == "4":
        if len(angka_list) == 0:
            print("Maaf belum ada data untuk dihapus")
        else:
            print("Daftar angka sekarag", angka_list)
            hapus = int(input("Silahkan msukan angka yang ingin dihapus mulai dari index (0): "))
            if 0 <= hapus < len(angka_list):
                angka_list.pop(hapus)
                print("Selamat data anda berhasil dihapus")

            else:
                print("Maaf data anda tidak ditemukan")
    
    elif pilihanmu == "5":
        if len(angka_list) == 0:
            print("Maaf belum ada data sama sekali untuk di cek")

        else:
            total = sum(angka_list)
            if total % 2 != 0:
                print ("Maaf total angka ganjil tidak bisa di bagi dua")

            else:
                kiri = 0
                separuh = sum(angka_list) // 2
                hasil = False
                for a in angka_list:
                    kiri += a
                    if kiri == separuh:
                        hasil = True
                        break
                    print("Jadi hasilnya adalah", hasil)

    elif pilihanmu == "6":
        print ("Selamat program anda telah selesai, Terima Kasih")
