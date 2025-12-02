print("="*10," TUGAS 2 MODUL 7 ","="*10)

gudang = {}
while True :
    print("1. Lihat Barang")
    print("2. Cari Barang")
    print("3. Tambah Barang")
    print("4. Update Stok")
    print("5. Hapus Barang")
    print("6. Keluar")
    user = input("pilih menu 1-6: ")
    if user == "1":
        if not gudang : print("Kosong. ")
        for id, v in gudang.items(): print(id,"-", v)
    elif user == "2":
        id = input("ID: ")
        print(gudang.get(id, "Barang tidak ditemukan. "))
    elif user == "3":
        id = input("ID baru: ")
        if id in gudang: print("ID sudah ada. ")
        else:
            nama = input("Nama Barang: ")
            harga = float(input("Harga Barang: "))
            while True:
                stok = int(input("Jumlah stok: "))
                if stok > 0:
                    gudang[id] = [nama, harga, stok]
                    print("Barang ditambah. ")
                    break
                else:
                    print("Stok tidak Boleh 0 Atau Negatif")
                    continue

    elif user == "4":
        id = input("ID: ")
        if id not in gudang: print("Tidak ditemukan. ")
        else:
            ubah = int(input("Ubah stok (-/+): "))
            if gudang [id][2] + ubah < 0:
                print("Stok tidak boleh negatif! ")
            else:
                gudang[id][2] += ubah
                print("Stok diperbarui. ")
    elif user == "5":
        id = input("ID: ")
        print("Dihapus. " if gudang.pop(id, None) else "Tidak ditemukan. ")
    elif user == "6":
        break
    else:
        print("Silahkan Pilih Menu Menggunakan 1-6")
        continue