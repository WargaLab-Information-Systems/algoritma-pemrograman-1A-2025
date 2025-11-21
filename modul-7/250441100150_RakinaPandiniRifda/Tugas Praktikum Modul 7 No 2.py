# Menampilkan manajemen inventaris gudang dengan fitur CRUD.
database = {}
id_set = set()
jalan = True

def input_angka(pesan, tipe=int):
    while True:
        try:
            nilai = tipe(input(pesan))
            return nilai
        except ValueError:
            print("Input harus berupa angka! Coba lagi.")

def input_id(pesan):
    while True:
        ID = input(pesan)
        try:
            if ID == "":
                raise ValueError("kosong")
            int(ID)
            return ID
        except ValueError:
            print("ID hanya boleh berupa angka dan tidak boleh kosong! Coba lagi.")

def input_nama(pesan):
    while True:
        nama = input(pesan)
        try:
            int(nama)
            print("Nama barang tidak boleh berupa angka! Coba lagi.")
        except ValueError:
            if nama == "":
                print("Nama barang tidak boleh kosong!")
            else:
                return nama

while jalan:
    print("\n=== Menu Manajemen Gudang ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang")
    print("3. Tambah barang")
    print("4. Update stok")
    print("5. Hapus barang")
    print("6. Keluar")

    pilihan = input_angka("Pilih menu (1-6): ")

    #read
    if pilihan == 1:
        if not database:
            print("Tidak ada data.")
        else:
            for ID, data in database.items():
                print(f"ID:{ID} | Nama:{data[0]} | Harga:{data[1]} | Stok:{data[2]}")
    
    #read
    elif pilihan == 2:
        ID = input_id("Masukkan ID: ")
        if ID in database:
            print(database[ID])
        else:
            print("ID tidak ditemukan.")

    #create
    elif pilihan == 3:
        ID = input_id("ID baru: ")
        if ID in id_set:
            print("ID sudah ada.")
        else:
            nama = input_nama("Nama barang: ")
            harga = input_angka("Harga: ", float)
            stok = input_angka("Stok: ", int)
            database[ID] = [nama, harga, stok]
            id_set.add(ID)
            print("Barang ditambahkan.")

    #update
    elif pilihan == 4:
        ID = input_id("ID: ")
        if ID not in database:
            print("ID tidak ditemukan.")
        else:
            stok_baru = input_angka("Perubahan stok (dalam bentuk 1/-1): ", int)
            if database[ID][2] + stok_baru < 0:
                print("Stok tidak boleh negatif!")
            else:
                database[ID][2] += stok_baru
                print("Stok diperbarui.")

    #delete
    elif pilihan == 5:
        ID = input_id("ID: ")
        if ID in database:
            del database[ID]
            id_set.remove(ID)
            print("Barang dihapus.")
        else:
            print("ID tidak ditemukan.")

    elif pilihan == 6:
        jalan = False
        print("Program selesai.")

    else:
        print("Pilihan menu tidak valid! Coba lagi.")