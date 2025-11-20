X = "SOAL NO 1"
print(X)

kontak = {}
huruf = "abcdefghijklmnopkrstuvwxyz"

def tampilkan_semua_kontak ():
    if not kontak:
        print("Belum ada kontak.")
    else:
        for nama, data in kontak.items():
            print(f"Nama: {nama}, Telepon: {data[0]}, Email: {data[1]}")

def cari_kontak ():
    nama = input("Masukkan nama atau email yang di cari: ")
    if nama in kontak:
        print(f"Nama: {nama}, Telepon: {kontak[nama][0]}, Email: {kontak[nama][1]}")
    else:
        print("maaf kontak tidak ditemukan")


def tambah_kontak():
    nama = input("Silahakan masukkan nama: ")
    Telepon = input("Silahakan masukkan no telepon: ")
    email = input ("Silahakan masukkan Email anda: @gmail.com ")
    print("Maaf Email harus mengandung @gmail.com  ")
    kontak[nama] = [Telepon, email]
    print ("kontak berhasil ditambahkan")

def perbarui_email():
    nama = input("Masukkan nama kontak: ")
    if nama in kontak:
        email_baru = input("Masukkan email baru: ")
        kontak[nama][1] = email_baru
        print("Email berhasil diperbarui.")
    else:
        print("Kontak tidak ditemukan.")

def hapus_kontak():
    nama = input("Masukkan nama yang ingin dihapus: ")
    if nama in kontak:
        del kontak[nama]
    else:
        print("Kontak tidak ditemukan.")

        print("Kontak berhasil dihapus.")
while True:
    print("\n-- PROGRAM KONTAK ---")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak")
    print("4. Update email kontak")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilihanmu = input("Pilih menu: ")

    if pilihanmu == "1":
        tampilkan_semua_kontak()
    elif pilihanmu == "2":
        cari_kontak()
    elif pilihanmu == "3":
        tambah_kontak()
    elif pilihanmu == "4":
        perbarui_email()
    elif pilihanmu == "5":
        hapus_kontak()
    elif pilihanmu == "6":
        break
    else:
        print("Input salah.")