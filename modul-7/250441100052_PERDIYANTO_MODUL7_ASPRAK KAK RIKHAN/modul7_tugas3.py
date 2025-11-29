data_kupon = {
    "p312":10,
    "123p":5
}

def tampil():
    for k, i in data_kupon.items():
        print(f"kode kupon: {k} {i} %")

def transaksi():
    harga = int(input("masukan harga barang "))
    jumlah = int(input("masukan jumlah barang "))
    total_sementara = harga * jumlah
    kode = input("masukan kode diskon ")
    temu = False
    for k, i in data_kupon.items():
        if k.lower() == kode.lower():
            temu = True
            del data_kupon[k]
            diskon = (total_sementara*i) / 100
            total_akhir = total_sementara - diskon
            return print(f"total setelah memasukan kode kupon {k} adalah {total_akhir}")
        
    if not temu:
        print(f"kupon tidak ditemukan total harga {total_sementara}")

while True:
    print("=== MENU  ===")
    print("1. Tampilkan semua diskon")
    print("2. Menghitung total bayar")
    print("3. keluar")

    pilihan = input("masukan nomor menu ")

    if pilihan == "1":
        tampil()
    elif pilihan == "2":
        transaksi()
    elif pilihan == "3":
        break
 