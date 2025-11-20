data = []
id_antrian = 1

while True:
    print("\n1. Tambah  2. Tampil  3. Hapus  4. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        try:
            nama = input("Nama pengunjung: ")
            santri = input("Nama santri: ")
            asal = input("Asal (Sumatra/Kalimantan/Jawa): ")

            if asal != "Sumatra" and asal != "Kalimantan" and asal != "Jawa":
                print("Asal tidak valid!")
                continue

            data.append([id_antrian, nama, santri, asal])
            print("ID:", id_antrian)
            id_antrian += 1
        except:
            print("Terjadi kesalahan input!")

    elif pilih == "2":
        print("\nDaftar Pengunjung:")
        if len(data) == 0:
            print("Belum ada data")
        else:
            for asal in ["Sumatra", "Kalimantan", "Jawa"]:
                for d in data:
                    if d[3] == asal:
                        print(d)
    elif pilih == "3":
        try:
            hapus_id = int(input("Masukkan ID yang mau dihapus: "))
            ketemu = False
            for d in data:
                if d[0] == hapus_id:
                    data.remove(d)
                    ketemu = True
                    print("Data dihapus")
                    break

            if not ketemu:
                print("ID tidak ditemukan")
        except:
            print("Input ID harus angka!")

    elif pilih == "4":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak ada, coba lagi.")
