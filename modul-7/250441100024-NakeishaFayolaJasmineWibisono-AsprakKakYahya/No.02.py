gudang = {}

while True :
    print("1. Lihat")
    print("2. Cari")
    print("3. Tambah")
    print("4. Update Stok")
    print("5. Hapus")
    print("6. Keluar")
    p = input("pilih menu 1-6: ")

    if p == "1":
        if not gudang: print("Kosong. ")
        for id, v in gudang.items(): print(id,"-", v)
    elif p == "2":
        id = input("ID: ")
        print(gudang.get(id, "Barang tidak ditemukan. "))
    elif p == "3":
        id = input("ID baru: ")
        if id in gudang: print("ID sudah ada. ")
        else:
            nama = input("Nama: ")
            while True:
                harga = float(input("Harga: "))
                if harga < 0:
                    print("Harga tidak boleh negatif! ")
                else:
                    break
            while True:
                stok = int(input("Stok: "))
                if stok > 0:
                    gudang[id] = [nama, harga, stok]
                    print("Barang ditambah. ")
                    break
                else:
                    print("Stok tidak boleh negatif!")
                    continue

    elif p == "4":
        id = input("ID: ")
        if id not in gudang: print("Tidak ditemukan. ")
        else:
            ubah = int(input("Ubah stok (-/+): "))
            if gudang [id][2] + ubah < 0:
                print("Stok tidak boleh negatif! ")
            else:
                gudang[id][2] += ubah
                print("Stok diperbarui. ")
    elif p == "5":
        id = input("ID: ")
        print("Dihapus. " if gudang.pop(id, None) else "Tidak ditemukan. ")
    elif p == "6":
        break