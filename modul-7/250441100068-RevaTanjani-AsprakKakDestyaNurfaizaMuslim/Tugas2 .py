inventaris= {
    "1":["Tomat","10000","7"]

}

def cek():
    if len(inventaris)==0:
        print("\n===Stok masih kosong===")
    else: 
        print("\n===================[INVENTARIS]===================")
        for id,data in inventaris.items():
            print(f"ID: {id} | Nama: {data[0]} | Harga: Rp.{data[1]} | Stok: {data[2]} | ")
        print("==================================================")

def tambah():
    id = input("masukkan ID barang: ")
    if id.isdigit():
        if id in inventaris:
            print("ID sudah ada, coba angka lain")
        else:
            nama = input("masukkan nama barang: ")
            harga = int(input("masukkan harga barang: "))
            stok = int(input("masukkan total barang: "))
            inventaris[id]= [nama,harga,stok]

def hapus():
    id = input("masukkan id barang yang ingin dihapus: ")
    if id in inventaris:
        del inventaris[id]
        print("barang berhasil dihapus")
    else:
        print("Id tidak ditemukan")

def cari():
    id = input("masukkan id barang yang ingin dicari: ")
    if id in inventaris:
        for id, data in inventaris.items():
            print("Id barang berhasil ditemukan!")
            print(f"\nID: {id} | Nama: {data[0]} | Harga: Rp.{data[1]} | Stok: {data[2]} | ")
    else:
        print("id tidak ditemukan")

def perbarui():
    id = input("masukkan id barang yang ingin diperbarui: ")
    if id in inventaris:
        print("\n| 1. Nama | 2. Harga | 3. Stok |")
        baru = input("apa yang ingin anda perbarui: ")


        if baru == "1" or baru.lower() == "nama":
            inventaris[id][0] = input("Masukkan nama baru: ")
            print("nama berhasil diperbarui")

        elif baru == "2" or baru.lower() == "harga":
            hargabaru = int(input("masukkan harga barang yang baru(+/-): "))
            hargalama = int(inventaris[id][1])

            if hargalama + hargabaru >= 0:
                inventaris[id][1] = hargalama + hargabaru
                print("Harga berhasil diperbarui")
            else: 
                print("Harga tidak boleh hingga negatif")

        elif baru == "3" or baru.lower() == "stok":
            perubahan = int(input("Masukkan perubahan stok (+/-): "))
            stok_lama = int(inventaris[id][2])

            if stok_lama + perubahan >= 0:
                inventaris[id][2] = stok_lama + perubahan
                print("harga berhasil diperbarui")
            else:
                print("Stok tidak boleh hingga negatif!")

        else:
            print("Pilihan tidak ada!")

    else:
        print("ID barang tidak ditemukan!")

while True:
    print("\n=====================[MENU UTAMA]====================")
    print("| 1. Cek | 2.Tambah | 3.hapus | 4.cari | 5.Perbarui |")
    menu = input ("pilih menu: ")

    if menu == "1" or menu == "cek" : cek()
    elif menu == "2" or menu == "tambah": tambah()
    elif menu == "3" or menu == "hapus": hapus()
    elif menu == "4" or menu == "stok": cari()
    elif menu == "5" or menu == "perbarui": perbarui()
    else: print("Menu tidak diketahui??????")