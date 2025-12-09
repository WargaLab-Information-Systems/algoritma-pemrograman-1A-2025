buku_kontak = []

def tambah_kontak():
    nama = input("Masukkan nama: ")
    for nama_buku in buku_kontak:
        if nama_buku['nama'] == nama:
            print("Nama sudah ada! Gunakan nama lain atau update kontak.")
            return
    nomor_telepon = int(input("Masukkan nomor telepon: "))
    email = input("Masukkan email: ")
    kontak = {
        "nama": nama,
        "nomor_telepon": nomor_telepon,
        "email": email
    }
    buku_kontak.append(kontak)
    print("Kontak berhasil ditambahkan!")

def tampilkan_kontak():
    if buku_kontak:
        for i,kontak in enumerate(buku_kontak, start=1):
            print(f"Kontak {i}:")
            print(f"  Nama: {kontak['nama']}")
            print(f"  Nomor Telepon: {kontak['nomor_telepon']}")
            print(f"  Email: {kontak['email']}")
    else:
        print("Buku kontak kosong.")

def update_kontak():
    nama = input("Masukkan nama kontak yang ingin diupdate: ")
    for kontak in buku_kontak:
        if kontak["nama"] == nama:
            nomor_telepon = int(input("Masukkan nomor telepon baru: "))
            email = input("Masukkan email baru: ")
            kontak["nomor_telepon"] = nomor_telepon
            kontak["email"] = email
            print("Kontak berhasil diupdate!")
            return
    print("Kontak tidak ditemukan.")

def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    for kontak in buku_kontak:
        if kontak["nama"] == nama:
            buku_kontak.remove(kontak)
            print("Kontak berhasil dihapus!")
            return
    print("Kontak tidak ditemukan.")
            

def cari_kontak():
    nama = input("Masukkan nama kontak yang ingin dicari: ")
    for kontak in buku_kontak:
        if kontak["nama"] == nama:
            print(f"Nama: {kontak['nama']}")
            print(f"Nomor Telepon: {kontak['nomor_telepon']}")
            print(f"Email: {kontak['email']}")
            return
    print("Kontak tidak ditemukan.")


while True:
    print("\nBuku Kontak")
    print("1. Tambah Kontak")
    print("2. Tampilkan Kontak")
    print("3. Update Kontak")
    print("4. Hapus Kontak")
    print("5. Cari Kontak")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == '1':
        tambah_kontak()
    elif pilihan == '2':
        tampilkan_kontak()
    elif pilihan == '3':
        update_kontak()
    elif pilihan == '4':
        hapus_kontak()
    elif pilihan == '5':
        cari_kontak()
    elif pilihan == '6':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")