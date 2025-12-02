kupon = {}
kupon_exp = {}

def main():
    
    while True:
        print("\nKasir Sederhana")
        print("1. Tambah Kupon Belanja")
        print("2. Lihat Kupon Belanja")
        print("3. Transaksi")
        print("4. Selesai")

        try:
            pilih = int(input("Pilih menu: "))
            if pilih == 1:
                tambah_kupon()
            elif pilih == 2:
                lihat_kupon()
            elif pilih == 3:
                transaksi()
            elif pilih == 4:
                print("Program selesai.")
                break
            else:
                print("Masukkan Pilihan yang benar!!\n")
        except:
            print("INPUT HARUS ANGKA!!\n")


def tambah_kupon():

    while True:
        input_kupon = input("Buat Kode Kupon: ")
        if input_kupon == "":
            print("INPUT TIDAK BOLEH KOSONG!!\n")
            continue
        
        cek_kupon_duplikat = input_kupon in kupon
        if cek_kupon_duplikat:
            print("KODE KUPON SUDAH TERDAFTAR!!")
            print("KODE KUPON TIDAK BOLEH DUPLIKAT.\n")
            continue
        while True:
            try:
                input_diskon_kupon = float(input("Masukkan Diskon Kupon (Format harus '0.n' = nn% | '0.0n' = n%): "))
                if 0 < input_diskon_kupon < 1 and not input_diskon_kupon.is_integer():
                    break
                else:
                    print("Masukkkan Diskon Kupon sesuai formaat ('0.n' | '0.0n')\n")
                    continue
            except:
                print("INPUT HARUS ANGKA!!\n")
                continue

        kupon[input_kupon] = input_diskon_kupon
        print(kupon)
        
        pilih = input("\nIngin buat Kode Kupon lagi? (y/n) : ")
        if pilih == "y":
            continue
        else:
            pilih == "n"
            break
    return


def lihat_kupon():

    while True:
        try:
            pilih_opsi = int(input("1. Lihat Kupon Tersedia | 2. Lihat Kupon Expired | 3. kembali menu | PILIH : "))
        except:
            print("INPUT HARUS ANGKA!!")
            continue

        if pilih_opsi == 1:
            cek_data = False
            print("\nList Kode Kupon yang Tersedia")
            for list_kupon, diskon_kupon in kupon.items():
                print(f"\nKode Kupon : {list_kupon}")
                print(f"Diskon Kupon : {diskon_kupon}\n")
                cek_data = True
            if not cek_data:
                print("Tidak ada Kupon yang Tersedia.\n")
                break
        
        elif pilih_opsi == 2:
            print("\nList Kode Kupon yang sudah terpakai")
            cek_data = False
            for list_kupon_exp, diskon_kupon_exp in kupon_exp.items():
                print(f"\nKode Kupon : {list_kupon_exp}")
                print(f"Diskon Kupon : {diskon_kupon_exp}\n")
                cek_data = True
            if not cek_data:
                print("Belum ada kode kupon yang terpakai.\n")
                break
                
        elif pilih_opsi == 3:
            break
        else:
            print("Masukkan Pilihan yang benar!!\n")
            continue
    return

def transaksi():
    while True:
        try:
            total_belanja = int(input("Masukkan Total belanja : "))
        except:
            print("INPUT HARUS ANGKA!!\n")
            continue
        
        while True:
            pilih_transaksi = input("Apakah pembeli menggunakan kupon ? (y/n) : ").lower()

            if pilih_transaksi == "n":
                print(f"Total belanja adalah : Rp{total_belanja}")
                return

            # Pembeli pakai kupon
            elif pilih_transaksi == "y":
                if not kupon:
                    print("Tidak ada Kupon yang Tersedia.\n")
                    print(f"Total belanja adalah : Rp{total_belanja}")
                    return
                
                kode_kupon = input("Masukkan kode kupon: ")
                if kode_kupon == "":
                    print("INPUT TIDAK BOLEH KOSONG!!\n")
                    continue

                if kode_kupon in kupon_exp:
                    print("KODE TERSEBUT SUDAH TERPAKAI!\n")
                    continue

                if kode_kupon not in kupon:
                    print("Kode kupon tidak ditemukan!\n")
                    continue

                diskon = kupon[kode_kupon]
                setelah_diskon = total_belanja - (total_belanja * diskon)

                print(f"Mendapatkan diskon {int(diskon * 100)}% dari Kupon")
                print(f"Total belanja setelah diskon: Rp{setelah_diskon}")

                kupon_exp[kode_kupon] = diskon
                kupon.pop(kode_kupon)

                return
            
            else:
                print("Masukkan hanya 'y' atau 'n'!\n")
                continue


main()
