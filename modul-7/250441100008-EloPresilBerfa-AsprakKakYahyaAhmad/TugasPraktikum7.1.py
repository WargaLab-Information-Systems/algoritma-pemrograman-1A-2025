kontak = {} 

def menu():
    print("===Menu Contact Book===")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak berdasarkan nama")
    print("3. Tambah kontak baru")
    print("4. Update email kontak")
    print("5. Hapus kontak")
    print("6. Keluar")

def tampilkan():
    if not kontak:
        print("Tidak ada kontak tersimpan.")
    else:
        print("Daftar Kontak:")
        for name, details in kontak.items():
            print(f"Nama: {name}, Nomor Telepon: {details[0]}, Email: {details[1]}")

def cari():
    name = input("Masukkan nama kontak yang dicari: ").strip()
    if name in kontak:
        details = kontak[name]
        print(f"Nama: {name}, Nomor Telepon: {details[0]}, Email: {details[1]}")
    else:
        print("Kontak tidak ditemukan.")
        
def tambah():
    name = input("Masukkan nama kontak: ").strip()
    if name in kontak:
        print("Kontak dengan nama tersebut sudah ada.")
        return
    phone = input("Masukkan nomor telepon: ").strip()
    if not phone.isdigit():
            print("Nomor telepon harus berupa angka saja.")
            return
    if len(phone) > 12:
            print("Nomor telepon tidak boleh lebih dari 12 digit.")
            return
    email = input("Masukkan email: ").strip()
    kontak[name] = [phone, email]
    print("Kontak berhasil ditambahkan.")
    
def update():
    name = input("Masukkan nama kontak yang ingin diupdate: ").strip()
    if name not in kontak:
        print("Kontak tidak ditemukan.")
        return
    
    new_email = input("Masukkan email baru (gunakan @gmail.com): ").strip()

    if new_email[-10:] != "@gmail.com":
        print("Email harus menggunakan domain @gmail.com")
        return

    kontak[name][1] = new_email
    print("Email berhasil diupdate.")

def hapus():
    name = input("Masukkan nama kontak yang ingin dihapus: ").strip()
    if name not in kontak:
        print("Kontak tidak ditemukan.")
        return
    del kontak[name]
    print("Kontak berhasil dihapus.")

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
        print("Terima kasih telah menggunakan Contact Book!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
