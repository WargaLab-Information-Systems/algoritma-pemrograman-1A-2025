kontak = {}

def tambah_kontak():
    while True:
        try:
            nama = input("Nama: ")
            if nama in kontak:
                print("kontak sudah tersedia,silahkan masukkan yang lain")
                continue
            telepon = int(input("Telepon: "))
            email = input("Email: ") 
            kontak[nama] = [telepon, email]
            print("Kontak berhasil ditambahkan!\n")
            return
        except :
            print("nomer telepon harus berupa angka")
            continue

def update_email():
    nama = input("Masukkan nama kontak: ")
    if nama in kontak:
        email_baru = input("Masukkan email baru: ")
        kontak[nama][1] = email_baru
        print("Email berhasil diperbarui!\n")
    else:
        print("Kontak tidak ditemukan.\n")

def cari_kontak():
    nama = input("Masukkan nama kontak: ")
    if nama in kontak:
        print(f"Telepon: {kontak[nama][0]}")
        print(f"Email  : {kontak[nama][1]}\n")
    else:
        print("Kontak tidak ditemukan.\n")

def tampilkan_semua():
    if not kontak:
        print("Belum ada kontak.\n")
        return
    for nama, info in kontak.items():
        print(f"Nama : {nama}")
        print(f"Telepon : {info[0]}")
        print(f"Email : {info[1]}\n")

def hapus_kontak():
    nama = input("Nama kontak yang akan dihapus: ")
    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus.\n")
    else:
        print("Kontak tidak ditemukan.\n")

while True:
    print("=== CONTACT BOOK ===")
    print("1.Tambah kontak")
    print("2.Update email kontak")
    print("3.Cari kontak")
    print("4.Tampilkan semua kontak")
    print("5.Hapus kontak")
    print("6.Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_kontak()
    elif pilih == "2":
        update_email()
    elif pilih == "3":
        cari_kontak()
    elif pilih == "4":
        tampilkan_semua()
    elif pilih == "5":
        hapus_kontak()
    elif pilih == "6":
        print("Program selesai.terima kasih")
        break
    else:
        print("Pilihan tidak valid.\n")
