print("="*10, " PROJEK AKHIR PRAKTIKUM ", "="*10)

# MENU
Makanan = {
    "Nasi Goreng": [15000, 10],
    "Ayam Geprek": [18000, 8],
    "Bakso": [12000, 12]
}
Minuman = {
    "Es Teh": [5000, 20],
    "Kopi Hitam": [8000, 10],
    "Jus Mangga": [12000, 6]
}
# Menampilkan Menu
def tampilkan_menu():
    print("\n--- MENU MAKANAN ---")
    for nama, data in Makanan.items():
        print(f"{nama} - Rp{data[0]}  Stok: {data[1]}")

    print("\n--- MENU MINUMAN ---")
    for nama, data in Minuman.items():
        print(f"{nama} - Rp{data[0]}  Stok: {data[1]}")

# Fitur CRUD
def Tambah_menu(menu):
    nama = input("Nama item baru: ").title()
    if nama in menu:
        print("Item sudah ada!")
        return 
    while True:
        harga_input = input("Harga: ")
        if not harga_input.isdigit():
            print("Harga harus berupa angka dan tidak boleh negatif!")
            continue
        harga = int(harga_input)
        if harga <= 0:
            print("Harga harus lebih dari 0!")
            continue
        break
    while True:
        stok_input = input("Stok: ")
        if not stok_input.isdigit():
            print("Stok harus berupa angka dan tidak boleh negatif!")
            continue
        stok = int(stok_input)
        if stok < 0:
            print("Stok tidak boleh negatif!")
            continue
        break
    menu[nama] = [harga, stok]
    print("Item berhasil ditambahkan!")

def update_item(menu):
    nama = input("Nama item yang akan diupdate: ").title()
    if nama not in menu:
        print("Item tidak ditemukan!")
        return
    while True:
        harga_input = input("Harga baru: ")
        if not harga_input.isdigit():
            print("Harga harus berupa angka dan tidak boleh negatif!")
            continue
        harga = int(harga_input)
        if harga <= 0:
            print("Harga harus lebih dari 0!")
            continue
        break
    while True:
        stok_input = input("Stok baru: ")
        if not stok_input.isdigit():
            print("Stok harus berupa angka dan tidak boleh negatif!")
            continue
        stok = int(stok_input)
        if stok < 0:
            print("Stok tidak boleh negatif!")
            continue
        break
    menu[nama] = [harga, stok]
    print("Item berhasil diupdate!")

def delete_item(menu):
    nama = input("Nama item yang akan dihapus: ").title()
    if nama in menu:
        del menu[nama]
        print("Item berhasil dihapus!")
    else:
        print("Item tidak ditemukan!")

def beli():
    tampilkan_menu()
    pesanan = {}
    total_harga = 0
    while True:
        item = input("\nMasukkan nama item (atau 'selesai'): ").title()
        if item.lower() == "selesai":
            break
        # Validasi item
        if item in Makanan:
            menu = Makanan
        elif item in Minuman:
            menu = Minuman
        else:
            print("Item tidak ada di menu!")
            continue
        if menu[item][1] == 0:
            print(f"Stok {item} sudah HABIS! Silakan pilih item lain.")
            continue
        while True:
            jumlah = input("Masukkan Jumlah Pesanan: ")
            if not jumlah.isdigit():
                print("Jumlah harus berupa angka Dan Tidak Booleh Negatif")
                continue
            jumlah = int(jumlah)
            if jumlah > menu[item][1]:
                print("Stok tidak cukup!")
                continue      
            break
        menu[item][1] -= jumlah
        subtotal = jumlah * menu[item][0]
        pesanan[item] = [jumlah, subtotal]
        total_harga += subtotal
        print(f"Ditambahkan: {item} x{jumlah} = Rp{subtotal}")

    print("\n------ STRUK PEMBELIAN -------")
    for item, data in pesanan.items():
        print(f"{item} x{data[0]} = Rp{data[1]}")
    print(f"TOTAL BAYAR: Rp{total_harga}")
    print("------------------------------\n")

# Menu Utama
while True:
    print("""
------ MENU UTAMA ------
1. Lihat Menu
2. Tambah Item (CRUD)
3. Update Item (CRUD)
4. Hapus Item (CRUD)
5. Beli Makanan/Minuman
6. Keluar
-----------------------
""")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tampilkan_menu()
    elif pilihan == "2":
        jenis = input("Tambah di (Makanan/Minuman)? ").title()
        if jenis == "Makanan":
            Tambah_menu(Makanan)
        elif jenis == "Minuman":
            Tambah_menu(Minuman)
        else:
            print("Pilihan tidak valid!")
    elif pilihan == "3":
        jenis = input("Update di (Makanan/Minuman)? ").title()
        if jenis == "Makanan":
            update_item(Makanan)
        elif jenis == "Minuman":
            update_item(Minuman)
        else:
            print("Pilihan tidak valid!")
    elif pilihan == "4":
        jenis = input("Hapus di (Makanan/Minuman)? ").title()
        if jenis == "Makanan":
            delete_item(Makanan)
        elif jenis == "Minuman":
            delete_item(Minuman)
        else:
            print("Pilihan tidak valid!")
    elif pilihan == "5":
        beli()
    elif pilihan == "6":
        print("Terima kasih telah menggunakan program!")
        break
    else:
        print("Pilihan tidak valid")
