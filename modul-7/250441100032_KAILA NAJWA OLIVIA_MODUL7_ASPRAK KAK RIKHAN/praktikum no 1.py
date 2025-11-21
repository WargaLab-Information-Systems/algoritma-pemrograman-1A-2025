# Program Buku Kontak menggunakan Dictionary
# Format penyimpanan:
# kontak = { "Nama": ["nomor telepon", "Email"] }
kontak = {}
au
def tampilkan_semua():
    if not kontak:
        print("\nBelum ada data kontak.\n")
    else:
        print("\n=== DAFTAR KONTAK ===")
        for nama, info in kontak.items():
            print(f"No.telepon : {info[0]}")
            print(f"nama       : {nama}")
            print(f"Email      : {info[1]}")
            print("-----------------------------")
        print()
        
def cari_kontak():
    nomor_telepon = input("Masukkan nomor telepon yang dicari: ")
    ditemukan = False
    for nama, info in kontak.items():
        if info[0] == nomor_telepon :  
            print("\nKontak ditemukan:")
            print(f"Nama       : {nama}")
            print(f"No. telepon: {info[0]}")
            print(f"Email      : {info[1]}\n")
            ditemukan = True
            break  
    if not ditemukan:
        print("\nKontak tidak ditemukan.")

def tambah_kontak():
    nama = input("Masukkan nama kontak yang akan ditambahkan: ")
    if nama in kontak:
        print("\nNama sudah ada, tidak bisa ditambahkan.\n")
        return
    while True:
        nomor_telepon = input("Masukkan nomor telepon: ")
        if nomor_telepon.isdigit() and len(nomor_telepon) >= 10:
            print("nomor telepon sudah ditambah!")
            break
        else:
            print("Nomor telepon tidak valid! Harus berupa angka dan minimal 10 digit.")
            continue
    email = input("Masukkan email: ")

    kontak[nama] = [nomor_telepon, email]
    print("\nKontak berhasil ditambahkan!\n")

def perbarui_email():
    nama = input("Masukkan nama kontak yang ingin diperbarui emailnya: ")

    if nama not in kontak:
        print("\nKontak tidak ditemukan.\n")
        return

    email_baru = input("Masukkan email baru: ")
    kontak[nama][1] = email_baru
    print("\nEmail berhasil diperbarui!\n")

def hapus_kontak():
    nama = input("Masukkan nama yang ingin dihapus: ")

    if nama not in kontak:
        print("\nKontak tidak ditemukan.\n")
        return

    del kontak[nama]
    print("\nKontak berhasil dihapus!\n")

# ==========================
#        MENU UTAMA
# ==========================
while True:
    print("=== BUKU KONTAK ===")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari kontak ")
    print("3. Tambah Kontak")
    print("4. Perbarui Email Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_semua()
    elif pilihan == "2":
        cari_kontak()
    elif pilihan == "3":
        tambah_kontak()
    elif pilihan == "4":
        perbarui_email()
    elif pilihan == "5":
        hapus_kontak()
    elif pilihan == "6":
        print("\nProgram selesai. Terima kasih!\n")
        break
    else:
        print("\nPilihan tidak valid. Coba lagi.\n")