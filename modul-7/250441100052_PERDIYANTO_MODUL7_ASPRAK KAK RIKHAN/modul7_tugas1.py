data_utama = {
    "Perdi": ["08123456789", "perdi@mail.com"],
    "Budi": ["082233445566", "budi@mail.com"]
}

def tampilkan():
    for nama, data in data_utama.items():
        print(f"Nama : {nama}")
        print(f"Nomor: {data[0]}")
        print(f"Email: {data[1]}")

def cari():
    nama = input("Masukkan nama kontak yang ingin dicari: ")
    temu = False
    for kunci,nilai in data_utama.items():
        if kunci.lower() == nama.lower():
            print("Kontak ditemukan:")
            print(f"Nama : {nama}")
            print(f"Nomor: {nilai[0]}")
            print(f"Email: {nilai[1]}")
            temu = True
    if not temu:
        print("Kontak tidak ditemukan.")

def tambah():
    nama = input("Nama kontak baru: ")
    if nama in data_utama:
        print("Kontak sudah ada")
        return
    nomor = input("Nomor telepon: ")
    if len(nomor) > 12:
        print("tidak boleh lebih dari 12")
        return
    email = input("Email: ")
    data_utama[nama] = [nomor, email]

def update():
    nama = input("Masukkan nama kontak yang ingin diperbarui emailnya: ")
    for k, i in data_utama.items():
        if k.lower() == nama.lower():
            email_baru = input("Masukkan email baru: ")
            data_utama[k][1] = email_baru
            print("Email berhasil diperbarui.")

def hapus():
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    hapus = ""
    for k, i in data_utama.items():
        if k.lower() == nama.lower():
            hapus = k
            break
    if hapus:   
        del data_utama[hapus]
    else:        
        print("Kontak tidak ada.")

while True:
    print("=== MENU  ===")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak")
    print("4. Update email")
    print("5. Hapus kontak")
    print("6. Keluar")
    pilihan = input("masukan nomor menu ")
    if pilihan == "1":
        tampilkan()
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
