print("="*50)
print("Nama : Elo Presil Berfa")
print("NIM : 250441100008")
print("="*50)

#Soal

#Buatlah simulasi sederhana dari mesin ATM yang meminta user untuk memasukkan PIN(XXYYY(X = 2 NIM awal, Y = 3 NIM terakhir)). User memiliki kesempatan 3 kali untuk memasukkan PIN yang benar. Jika PIN benar, Tampilkan pesan “PIN benar, akses diterima”, jika salah, maka tampilkan pesan “PIN salah, coba lagi”. Jika sudah 3 kali salah, tampilkan pesan “Akses ditolak, kartu diblokir”. PIN harus diinput dalam bentuk angka dan harus 5 digit.

#Jawaban

pinbenar = "25008"
kesempatan = 3

print("Selamat datang di ATM, silahkan pilih menu")
print("a. Menu Transaksi")
print("b. Keluar")

menu = input("Masukkan Pilihan (a/b): ")

if menu == "a":
    while kesempatan > 0:
        pininput = input("Masukkan 5 digit PIN: ")

        if len(pininput) != 5:
            print("PIN harus 5 digit!")
            kesempatan -= 1
        elif pininput == pinbenar:
            print("PIN benar, akses diterima.")
            print("Selamat bertransaksi!")
            break
        else:
            print("PIN salah!")
            kesempatan -= 1

        if kesempatan == 0:
            print("Akses ditolak, kartu diblokir.")
            break
else:
    print("Sampai jumpa lagi!")






print("="*50)