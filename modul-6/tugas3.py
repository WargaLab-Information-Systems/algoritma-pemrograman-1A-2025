# Program Dominic Szoboszlai
# CRUD list angka dan cek apakah bisa dibagi jadi dua bagian dengan jumlah sama

# List utama untuk menyimpan data angka
data_angka = []

# Fungsi CREATE - tambah angka
def tambah_data(angka):
    data_angka.append(angka)

# Fungsi READ - tampilkan semua angka
def tampil_data():
    print("Data angka:", data_angka)

# Fungsi UPDATE - ubah angka berdasarkan index
def ubah_data(index, angka_baru):
    if 0 <= index < len(data_angka):
        data_angka[index] = angka_baru
    else:
        print("Index tidak valid!")

# Fungsi DELETE - hapus angka berdasarkan index
def hapus_data(index):
    if 0 <= index < len(data_angka):
        data_angka.pop(index)
    else:
        print("Index tidak valid!")

# Fungsi CEK PEMBAGIAN menjadi dua bagian dengan jumlah sama
def cek_pembagian():
    total = 0
    for x in data_angka:   # hitung total manual tanpa sum()
        total += x

    # Jika total ganjil, pasti tidak bisa dibagi dua sama besar
    if total % 2 != 0:
        print("False (tidak bisa dibagi dua bagian sama besar)")
        return

    setengah = total // 2
    jumlah = 0
    # coba cari kombinasi bagian pertama yang jumlahnya sama dengan setengah total
    for x in data_angka:
        jumlah += x
        if jumlah == setengah:
            print("True (bisa dibagi dua bagian dengan jumlah sama)")
            return
    print("False (tidak bisa dibagi dua bagian sama besar)")

tambah_data(1)
tambah_data(2)
tambah_data(3)
tambah_data(2)
tampil_data()        # [1, 2, 3, 2]

cek_pembagian()      # True karena [1,2,3] dan [2] keduanya berjumlah 6/2=3

ubah_data(1, 5)      # ubah index ke-1 dari 2 jadi 5
tampil_data()        # [1, 5, 3, 2]
cek_pembagian()      # False

hapus_data(2)        # hapus angka index ke-2
tampil_data()
