data_gudang = {
    1:["kasur",140000,2],
    2:["kursi",100000,5]
}

def tampil():
    for i, n in data_gudang.items():
        print(f"barang id ke - {i}")
        print(f"nama barang: {n[0]}")
        print(f"harga barang: {n[1]}")
        print(f"stock barang: {n[2]}")

def update():
    id = int(input("masukan id barang yang ingin di update "))
    if id not in data_gudang:
        print(f"data baranaag id {id} tidak ada")
        return
    stock = int(input("masukan stock terbaru "))
    if stock < 0:
        print("stock tidak boleh kurang dari 0 ")
        return
    data_gudang[id][2] = stock

def tambah():
    id = int(input("masukan id barang baru "))
    if id in data_gudang:
        print(f"id {id} sudah ada di gudang")
        return
    nama = input("masukan nama barang yang baru ")
    harga = int(input("masukan harga barang baru "))
    stock = int(input("masukan stock barang baru "))
    if stock < 0:
        print("stock tidak boleh kurang dari 0 ")
        return
    data_gudang[id] = [nama,harga,stock]

def hapus():
    id = int(input("masukan id barang yang ingin di hapus "))
    if id not in data_gudang:
        print("id barang tidak sesuai")
        return
    del data_gudang[id]

def cari():
    id = int(input("masukan id barang yang ingin di cari "))
    if id in data_gudang:
        print(f"id {id}")
        print(f"nama barang: {data_gudang[id][0]}")
        print(f"harga barang: {data_gudang[id][1]}")
        print(f"stock barang: {data_gudang[id][2]}")
        return
    elif id not in data_gudang:
        print("data tidak ada")
        return

while True:
    print("=== MENU  ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang")
    print("3. Tambah barang")
    print("4. Update stock")
    print("5. Hapus barang")
    print("6. Keluar")
    pilihan = input("masukan nomor menu ")
    if pilihan == "1":
        tampil()
    elif pilihan == "2":
        cari()
    elif pilihan == "3":
        tambah()
    elif pilihan == "4":
        update()
    elif pilihan == "5":
        hapus()
    elif pilihan == "6":
        break
    else:
        print("Pilihan tidak valid!")





