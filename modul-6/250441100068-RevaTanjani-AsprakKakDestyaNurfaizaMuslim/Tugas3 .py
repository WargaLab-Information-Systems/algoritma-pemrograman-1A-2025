data = []

def tambah():
    try:
        angka = int(input("Tambah angka: "))
        data.append(angka)
        print("Ditambah!")
    except:
        print("Harus angka!")

def tampil():
    print("Data:", data)

def ubah():
    try:
        i = int(input("Index: "))
        angka = int(input("Nilai baru: "))
        data[i] = angka
        print("Diubah!")
    except:
        print("Input salah!")

def hapus():
    try:
        i = int(input("Index: "))
        data.pop(i)
        print("Dihapus!")
    except:
        print("Input salah!")

def cek():
    total = sum(data)
    if total % 2 != 0:
        print("False")
        return
    
    kiri = 0
    for x in data:
        kiri += x
        if kiri == total // 2:
            print("True")
            return
    
    print("False")

while True:
    print("\n1.Tambah 2.Tampil 3.Ubah 4.Hapus 5.Cek 6.Keluar")
    p = input("Pilih: ")
    if p == "1": tambah()
    elif p == "2": tampil()
    elif p == "3": ubah()
    elif p == "4": hapus()
    elif p == "5": cek()
    elif p == "6":
        print("Keluar...")
        break
    else:
        print("Salah pilih!")
