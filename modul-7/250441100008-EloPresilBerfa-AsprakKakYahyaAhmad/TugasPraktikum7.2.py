inventaris = {}

def menu():
    print("===Menu Inventaris Gudang===")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang Berdasarkan ID")
    print("3. Tambah Barang Baru")
    print("4. Update Stok Barang")
    print("5. Hapus Barang")
    print("6. Keluar")
    
def tampilkan():
    if not inventaris:
        print("Tidak ada Barang tersimpan.")
    else:
        print("Daftar Barang:")
        for id, details in inventaris.items():
            print(f"ID: {id}, Nama Barang: {details[0]}, Harga: {details[1]}, Stok: {details[2]}")

def cari():
    id = input("Masukkan nama Barang yang dicari: ").strip()
    if id in inventaris:
        details = inventaris[id]
        print(f"ID: {id}, Nama Barang: {details[0]}, Harga: {details[1]}, Stok: {details[2]}")
    else:
        print("Barang tidak ditemukan.")

def tambah():
    id = input("Masukkan ID barang : ").strip()
    if id in inventaris:
        print("Barang dengan ID tersebut sudah ada.")
        return
    barang = input("Masukkan Nama Barang: ").strip()
    harga = int(input("Masukkan Harga: "))
    stok = int(input("Masukkan Stok: "))
    if stok < 0:
        print("Stok tidak boleh negatif!")
        return
    inventaris[id] = [barang, harga, stok]
    print("Barang berhasil ditambahkan.")
    
def update():
    id = input("Masukkan ID barang yang ingin diperbarui stoknya: ").upper()
    if id in inventaris:
        stok_baru = int(input("Masukkan stok baru : "))
        stok_akhir = inventaris[id][2] + stok_baru

        if stok_akhir < 0:
            print("Stok tidak boleh negatif!")
            return
        
        inventaris[id][2] = stok_akhir
        print("Stok barang berhasil diperbarui!")
    else:
        print("Barang tidak ditemukan!")
        
def hapus():
    id = input("Masukkan id barang yang ingin dihapus: ").strip()
    if id not in inventaris:
        print("barang tidak ditemukan.")
        return
    del inventaris[id]
    print("barang berhasil dihapus.")

while True:
    menu()
    pilih = input("Pilih opsi (1-6): ").strip()
    
    if pilih == '1':
        tampilkan()
    elif pilih == '2':
        cari()
    elif pilih == '3':
        tambah()
    elif pilih == '4':
        update()
    elif pilih == '5':
        hapus()
    elif pilih == '6':
        print("Terima kasih telah menggunakan Program Inventaris!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")