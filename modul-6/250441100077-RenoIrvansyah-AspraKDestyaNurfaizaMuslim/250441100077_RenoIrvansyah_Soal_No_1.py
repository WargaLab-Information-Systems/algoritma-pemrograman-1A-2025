pengunjung = []
id_pengunjung = 1

def tambah_pengunjung():

    while True:
            print("="*50)
            global id_pengunjung
            cek_input = False

            nama_pengunjung = input("Masukkan Nama Pengunjung: ").title()
            for huruf in nama_pengunjung:
                    if huruf in ['0','1','2','3','4','5','6','7','8','9']:
                        cek_input = True
                        break 
            if cek_input:
                print("Input tidak boleh mengandung angka! Coba lagi.") 
                print("ULANGI INPUT DATA!!")
                continue

            nama_santri = input("Masukkan Nama Santri: ").title()
            for huruf in nama_santri:  
                    if huruf in ['0','1','2','3','4','5','6','7','8','9']:
                        cek_input = True
                        break 
            if cek_input:
                print("Input tidak boleh mengandung angka! Coba lagi.")
                print("ULANGI INPUT DATA!!")
                continue

            asal_pengunjung = input("Masukkan asal (Sumatra / Kalimantan / Jawa): ").title()
            
            if asal_pengunjung not in ["Sumatra", "Kalimantan", "Jawa"]:
                print("Masukkan asal yang sudah tertera!! (Sumatra / Kalimantan / Jawa)")
                print("ULANGI INPUT DATA!!")
                continue

            tambah_pengunjung = [id_pengunjung, nama_pengunjung, nama_santri, asal_pengunjung]
            pengunjung.append(tambah_pengunjung)
            print(f"Data pengunjung ke-{id_pengunjung} berhasil ditambahkan!\n")
            id_pengunjung += 1

            lanjut = input("Lanjut isi data? y/n : ")
            if lanjut == "y":
                continue
            elif lanjut == "n":
                break

def data_pengunjung():
    urutan = ["Sumatra", "Kalimantan", "Jawa"]
    for asal_daerah in urutan:
        print(f"\nDari {asal_daerah.upper()}:")
        cek_list = False
        for daftar in pengunjung:
            if daftar[3].lower() == asal_daerah.lower():
                print("_"*50)
                print(f"\nID Pengunjung :{daftar[0]}")
                print(f"Nama Pengunjung :{daftar[1]}")
                print(f"Nama Santri     :{daftar[2]}")
                print(f"Asal Pengunjung :{daftar[3]}")
                print("_"*50)
                cek_list = True
        if not cek_list:
            print("(Tidak ada data)")

def hapus_pengunjung():
    
    hapus_pengunjung = int(input("Masukkan ID Pengunjung yang ingin di hapus : "))
    cek_data = False
    for cari_pengunjung in pengunjung:
        if cari_pengunjung[0] == hapus_pengunjung:
            pengunjung.remove(cari_pengunjung)
            print(f"Data ID Pengunjung {hapus_pengunjung} Berhasil di hapus.")
            cek_data = True
            break
    if not cek_data:
        print(f"Data ID Pengunjung {hapus_pengunjung} tidak ditemukan!!")
        print("Silahkan periksa List Pengunjung terlebih dahulu!!")

def utama():
    while True:
        print("="*50)
        print("1. tambah data pengunjung | 2. lihat list pengunjung | 3. hapus data pengunjung | 4. Selesai")
        print("pilih sesuai angka")
        pilih = int(input("Masukkan pilihan : "))
        if pilih == 1:
            tambah_pengunjung()
        elif pilih == 2:
            data_pengunjung()
        elif pilih == 3:
            hapus_pengunjung()
        elif pilih == 4:
            print("Program selesai")
            break
        else:
            print("Masukkan Pilihan yang benar!!")
            continue

utama()
        