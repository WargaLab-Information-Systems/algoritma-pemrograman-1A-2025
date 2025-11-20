kontak = {}

def tampilkan_kontak():
    if not kontak:
        print("tidak ada data kontak.")
    else:
        print("-----DAFTAR KONTAK-----")
        for nama, data in kontak.items():
            print("nama: ", nama, "telepon:", data[0], "email:", data[1])
    
def cari_kontak():
    nama = input("masukkan nama kontak yang ingin dicari : ")
    if nama in kontak:
        print("telepon : ", kontak[nama][0], "email:", kontak[nama][1])
    else:
        print("kontak tidak ditemukan.")
    print()
def tambah_kontak():
    nama = input("masukkan nama kontak baru : ")
    if nama in kontak:
        print("nama kontak sudah ada! ")
        return
    
    telepon = int(input("massukan nomor telepon : "))
    email = input("masukkan email : ")
    kontak[nama] = [telepon, email]
    print("kontak berhasil ditambahkan")

def update_email():
    nama = input("masukkan nama kontak yang ingin diperbarui emailnya : ")
    if nama not in kontak:
        print("kontak tidak ditemukan")
        return
    email_baru = input("masukkan email baru : ")
    kontak[nama][1] = email_baru
    print("email berhasil diperbarui")

def hapus_kontak():
    nama = input("masukkan nama kontak yang ingin dihapus : ")
    if nama in kontak:
        del kontak[nama]
        print("kontak berhasil dihapus")
    else:
        print("kontak tidak ditemukan")

while True:
    print("-----MENU CONTACT BOOK-----")
    print("1. tampilkan semua kontak")
    print("2. cari kontak")
    print("3. tambah kontak")
    print("4. update email kontak")
    print("5. hapus kontak")

    pilih = input("pilih menu dari (1-6) : ")

    if pilih == "1":
        tampilkan_kontak()
    elif pilih == "2":
        cari_kontak()
    elif pilih == "3":
        tambah_kontak()
    elif pilih == "4":
        update_email()
    elif pilih == "5":
        hapus_kontak()
    else:
        print("pilihan tidak valid!")