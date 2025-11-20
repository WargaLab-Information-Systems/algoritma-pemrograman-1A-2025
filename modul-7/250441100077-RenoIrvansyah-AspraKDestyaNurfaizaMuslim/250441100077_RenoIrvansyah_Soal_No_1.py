kontak = {}

def main():

    while True:
        print("\nCONTACT LIST")
        print("1. Tambah Kontak")
        print("2. Lihat Kontak")
        print("3. Update Kontak")
        print("4. Hapus Kontak")
        print("5. Selesai")

        try:
            pilih = int(input("Pilih menu: "))
            if pilih == 1:
                tambah_kontak()
            elif pilih == 2:
                lihat_kontak()
            elif pilih == 3:
                update_kontak()
            elif pilih == 4:
                hapus_kontak()
            elif pilih == 5:
                print("Program selesai.")
                break
            else:
                print("Masukkan Pilihan yang benar!!\n")
        except:
            print("INPUT HARUS ANGKA!!\n")

def tambah_kontak():
    
    while True:
        input_nama = input("Masukkan Nama: ")
        if input_nama == "":
            print("INPUT TIDAK BOLEH KOSONG!!\n")
            continue
        
        cek_nama_duplikat = input_nama in kontak
        if cek_nama_duplikat:
            print("NAMA SUDAH TERDAFTAR!!")
            print("Silahkan masukkan nama lain.\n")
            continue
        
        while True:
            try:
                cek_input = False
                input_nomor = input("Masukkan Nomor Telepon: ")
                for angka in input_nomor:
                    if angka in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                        cek_input = True
                        break
                if cek_input:
                    print("Input tidak boleh mengandung huruf!, Coba lagi!") 
                    print("ULANGI INPUT DATA!!")
                    continue
                validasi_nomor = len(input_nomor)
                if validasi_nomor > 13:
                    print("Nomor tidak boleh melebihi 13 digit")
                    continue
            except:
                print("INPUT HARUS ANGKA!!\n")
                continue

            while True:
                input_email = input("Masukkan Email: ")
                if "@" in input_email and "." in input_email and not input_email.startswith("@") and not input_email.endswith("."):
                    break
                else:
                    print("Format email tidak valid! Contoh: nama@gmail.com")
                    continue

            kontak[input_nama] = input_nomor, input_email
            # print(kontak)
            break

        pilih = input("Tambah kontak lagi? (y/n): ").lower()
        if pilih == "y":
            continue
        else:
            pilih == "n"
            break
    return

def lihat_kontak():
    
    while True:
        try:
            pilih_opsi_kontak = int(input("1. tampilkan semua kontak | 2. cari kontak | 3. kembali menu | PILIH : "))

            if pilih_opsi_kontak == 1:
                print("\nDaftar Kontak yang Tersedia: ")
                for list in kontak:
                    print(f"\nNama: {list}")
                    print(f"Nomor Telepon: {kontak[list][0]}")
                    print(f"Email: {kontak[list][1]}\n")
                if not kontak:
                    print("Tidak ada kontak yang tersimpan.")
                    break
            
            elif pilih_opsi_kontak == 2:
                cari_kontak = input("masukkan nama yang ingin dicari : ")
                if cari_kontak in kontak:
                    print("\nKontak ditemukan: ")
                    print(f"\nNama: {cari_kontak}")
                    print(f"Nomor Telepon: {kontak[cari_kontak][0]}")
                    print(f"Email: {kontak[cari_kontak][1]}\n")
                else:
                    print("Kontak tidak ditemukan.")
                    break

                
            elif pilih_opsi_kontak == 3:
                break
            else:
                print("Masukkan Pilihan yang benar!!\n")
                continue

        except:
            print("INPUT HARUS ANGKA")
            continue
    return

def update_kontak():
    while True:
        print("\nDaftar Kontak yang Tersedia: ")
        for list in kontak:
            print(f"\nNama: {list}")
            print(f"Nomor Telepon: {kontak[list][0]}")
            print(f"Email: {kontak[list][1]}")
        if not kontak:
            print("Tidak ada kontak yang tersimpan.")
            break

        nama_kontak = input("Masukkan Nama Kontak yang ingin di-update datanya: ")
        cek_kontak = False
        for cari_kontak in kontak:
            if cari_kontak == nama_kontak:
                print(f"Data kontak {nama_kontak} ditemukan.\n")
                try:
                    print("ingin update data kontak ini? ...")
                    pilih_update= int(input("1. update nomor telepon | 2. update email | 3. batal update |PILIH : "))
                    if pilih_update == 1:
                        while True:
                            try:
                                input_update_nomor = int(input("Masukkan Nomor Telepon Baru: "))
                                kontak.update({cari_kontak: (input_update_nomor, kontak[cari_kontak][1])})
                                print(f"Data kontak {cari_kontak} berhasil di update.")
                                break
                            except:
                                print("INPUT HARUS ANGKA!!\n")
                                continue
                    elif pilih_update == 2:
                        while True:
                            input_email = input("Masukkan Email: ")
                            if "@" in input_email and "." in input_email and not input_email.startswith("@") and not input_email.endswith("."):
                                kontak.update({cari_kontak: (kontak[cari_kontak][0], input_email)})
                                print(f"Data kontak {cari_kontak} berhasil di update.")
                                break
                            else:
                                print("Format email tidak valid! Contoh: nama@gmail.com")
                                continue
                    elif pilih_update == 3:
                        break
                    else:
                        print("Masukkan Pilihan yang benar!!\n")
                        continue
                except:
                    print("INPUT HARUS ANGKA!!\n")
                    continue
                cek_kontak = True
                break
        if not cek_kontak:
            print(f"Data kontak {nama_kontak} tidak ditemukan.")
    return

def hapus_kontak():

    nama_kontak = input("Masukkan Nama Kontak yang ingin dihapus: ")
    cek_kontak = False
    for cari_kontak in kontak:
        if cari_kontak == nama_kontak:
            kontak.pop(cari_kontak)
            print(f"Data kontak {nama_kontak} berhasil dihapus.")
            cek_kontak = True
            break
    if not cek_kontak:
        print(f"Data kontak {nama_kontak} tidak ditemukan.")
    return

main()
