# id_barang = 1
barang = {}

def main():

    while True:
        print("\nInventaris Gudang")
        print("1. Tambah Barang")
        print("2. Lihat Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Selesai")

        try:
            pilih = int(input("Pilih menu: "))
            if pilih == 1:
                tambah_barang()
            elif pilih == 2:
                lihat_barang()
            elif pilih == 3:
                update_barang()
            elif pilih == 4:
                hapus_barang()
            elif pilih == 5:
                print("Program selesai.")
                break
            else:
                print("Masukkan Pilihan yang benar!!\n")
        except:
            print("INPUT HARUS ANGKA!!\n")


def tambah_barang():

    while True:
        # global id_barang
        try:
            input_id_barang = int(input("Masukkan ID untuk Barang: "))
            cek_id_duplikat = input_id_barang in barang
            if cek_id_duplikat:
                print("ID BARANG SUDAH TERDAFTAR!!")
                print("Silahkan masukkan ID yang berbeda.\n")
                continue
        except:
            print("INPUT HARUS ANGKA!!\n")
            continue

        input_barang = input("\nMasukkan Nama Barang: ")
        if input_barang == "":
            print("INPUT TIDAK BOLEH KOSONG!!\n")
            continue

        try:
            input_harga = int(input("Masukkan Harga Barang: "))
        except:
            print("INPUT HARUS ANGKA!!\n")
            continue

        try:
            input_stok_barang = int(input("Masukkan Stok Barang: "))
        except:
            print("INPUT HARUS ANGKA!!\n")
            continue

        barang[input_id_barang] = input_barang, input_harga, input_stok_barang
        print(f"Data Barang baru berhasil ditambahkan.")
        # id_barang += 1
            # print(barang)

        pilih = input("\nTambah kontak lagi? (y/n): ").lower()
        if pilih == "y":
            continue
        else:
            pilih == "n"
            break
    return

def lihat_barang():

    while True:
        try:
            pilih_opsi_barang = int(input("1. tampilkan semua barang | 2. cari Barang berdasarkan ID | 3. kembali menu | PILIH : "))
            if pilih_opsi_barang == 1:
                cek_list = False
                print("\nList Barang yang Tersedia: ")
                for list in barang:
                    print(f"\nID barang: {list}")
                    print(f"Nama Barang: {barang[list][0]}")
                    print(f"Harga Barang: {barang[list][1]}")
                    print(f"Stok: {barang[list][2]}\n")
                    cek_list  =True
                if not cek_list:
                    print("\nTidak ada barang yang tersimpan!!")
                    break
            
            elif pilih_opsi_barang == 2:
                cari_barang = int(input("masukkan ID barang yang ingin dicari : "))
                if cari_barang in barang:
                    print("\nBarang ditemukan: ")
                    print(f"\nID Barang: {cari_barang}")
                    print(f"Nomor Barang: {barang[cari_barang][0]}")
                    print(f"Harga Barang: {barang[cari_barang][1]}")
                    print(f"Stok: {barang[cari_barang][2]}\n")
                else:
                    print("Barang tidak ditemukan.")
                    break

            elif pilih_opsi_barang == 3:
                break
            else:
                print("Masukkan Pilihan yang benar!!\n")
                continue

        except:
            print("INPUT HARUS ANGKA")
            continue        

    return

def update_barang():

    while True:
        print("\nList Barang yang Tersedia: ")
        for list in barang:
            print(f"\nID barang: {list}")
            print(f"Nama Barang: {barang[list][0]}")
            print(f"Harga Barang: {barang[list][1]}")
            print(f"Stok: {barang[list][2]}\n")
        if not barang:
            print("Tidak ada Barang yang tersimpan.")
            break

        try:
            cek_id_barang = int(input("Masukkan ID Barang ingin di-update datanya: "))
            cek_barang = False
            for cari_barang in barang:
                if cari_barang == cek_id_barang:
                    print(f"Data Barang dengan ID-{cek_id_barang} ditemukan.\n")
                    print(f"\nID barang: {list}")
                    print(f"Nama Barang: {barang[list][0]}")
                    print(f"Harga Barang: {barang[list][1]}")
                    print(f"Stok: {barang[list][2]}\n")
                    try:
                        print("ingin update data barang ini? ...")
                        pilih_update= int(input("1. Update Nama Barang | 2. Update Harga Barang | 3. Tambah Stok Barang | 4. Ambil Stok Barang | 5. Batal Update Barang | PILIH : "))
                        if pilih_update == 1:
                            while True:
                                input_update_nama = (input("Masukkan Nama Barang Baru: "))
                                if input_update_nama == "":
                                    print("INPUT TIDAK BOLEH KOSONG!!\n")
                                    continue
                                barang.update({cari_barang: (input_update_nama, barang[cari_barang][1], barang[cari_barang][2])})
                                print(f"Data barang {cari_barang} berhasil di update.")
                                break

                        elif pilih_update == 2:
                            while True:
                                try:
                                    input_update_harga = int(input("Masukkan Harga Barang terbaru: "))
                                    barang.update({cari_barang: (barang[cari_barang][0], input_update_harga, barang[cari_barang][2])})
                                    print(f"Data barang {cari_barang} berhasil di update.")
                                    break
                                except:
                                    print("INPUT HARUS ANGKA!!\n")
                                    continue

                        elif pilih_update == 3:
                            while True:
                                try:
                                    tambah_stok_barang = int(input("Tambah Stok Barang : "))
                                    tambah_stok = barang[cari_barang][2] + tambah_stok_barang
                                    barang.update({cari_barang: (barang[cari_barang][0], barang[cari_barang][1], tambah_stok)})
                                    print(f"Data barang {cari_barang} berhasil di update.")
                                    break
                                except:
                                    print("INPUT HARUS ANGKA!!\n")
                                    continue

                        elif pilih_update == 4:
                            while True:
                                try:
                                    ambil_stok_barang = int(input("Ambil Stok Barang : "))
                                    ambil_stok = barang[cari_barang][2] - ambil_stok_barang
                                    if ambil_stok >= 0:
                                        barang.update({cari_barang: (barang[cari_barang][0], barang[cari_barang][1], ambil_stok)})
                                        print(f"Data barang {cari_barang} berhasil di update.")
                                        break
                                    elif ambil_stok <= 0:
                                        print("STOK TIDAK DAPAT DIAMBIL LEBIH DARI JUMLAH STOK YANG ADA!!")
                                        continue
                                except:
                                    print("INPUT HARUS ANGKA!!\n")
                                    continue

                        elif pilih_update == 5:
                            break
                        else:
                            print("Masukkan Pilihan yang benar!!\n")
                            continue
                    except:
                        print("INPUT HARUS ANGKA!!\n")
                        continue
                    cek_barang = True
                    break
            if not cek_barang:
                print(f"Data Barang {cek_id_barang} tidak ditemukan.")
        except:
            print("INPUT HARUS ANGKA!!\n")
            continue
        return

def hapus_barang():
    while True:
        try:
            pilih_hapus = int(input("1. Hapus berdasarkan ID Barang | 2. Hapus Berdasarkan Nama Barang | 3. Batal Hapus Barang | Pilih: "))

            if pilih_hapus == 1:
                try:
                    hapus_barang_id = int(input("\nMasukkan ID Barang yang ingin dihapus data nya : "))
                    cek_barang = False
                    for cari_barang in barang:
                        if cari_barang == hapus_barang_id:
                            barang.pop(cari_barang)
                            print(f"Data Barang {hapus_barang_id} berhasil dihapus.")
                            cek_barang = True
                            break
                    if not cek_barang:
                        print(f"Data Barang {hapus_barang_id} tidak ditemukan.")
                except:
                    print("INPUT HARUS ANGKA!!\n")
            
            elif pilih_hapus == 2:
                hapus_barang_nama = input("\nMasukkan nama barang yang ingin dihapus data nya : ")
                cek_barang = False

                for cari_barang, cari_nama in list(barang.items()):
                    if cari_nama[0] == hapus_barang_nama:
                        barang.pop(cari_barang)
                        print(f"Data Barang {hapus_barang_nama} berhasil dihapus\n")
                        cek_barang = True
                        break
                if not cek_barang:
                    print(f"Data Barang {hapus_barang_nama} tidak ditemukan.")

            elif pilih_hapus == 3:
                break
            else:
                print("Masukkan Pilihan yang benar!!\n")
        except:
            print("INPUT HARUS ANGKA!!\n")
    return

main()