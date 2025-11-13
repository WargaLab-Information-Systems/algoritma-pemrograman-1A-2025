X = ("SOAL NO 1")
print(X)

id_antrian = 1

data_kunjungan = []

while True:
    print ("--SISTEM KUNJUNGAN SANTRI PONDOK PESANTREN ANNUQAYAH--")
    print ("1. Tambahkan data pengunjung")
    print ("2. Tampilkan seluruh daftar pengunjung")
    print ("3. Hapus data pengunjung")
    print ("4. Keluar")
    pilihanmu = input("Silahakan masukan pilihanmu (1-4): ")

    if pilihanmu == "1" :
        print("Tambahakan data kunjungan")
        nama_pengunjung = input("Silahakan masukkan nama pengunjung: ")
        nama_santri = input("Silahakan masukkan nama santri: ")
        daerah_asal = input("silahakan masukkan daerah asalnya: (Sumatera, Kalimantan, Jawa)").lower()

        data = [id_antrian, nama_pengunjung, nama_santri, daerah_asal]
        data_kunjungan.append(data)
        print("data berhasil ditambahkan dengan no ID: ", id_antrian)
        id_antrian +=1

    elif pilihanmu == "2":
        if len (data_kunjungan) == 0 :
            print ("Maaf belum ada data kunjungannya")
        else:
            print("Daftar kunjungan berdasarkan daerah asal santri")
            for data in data_kunjungan :
                print ("ID:", data[0])
                print ("Pengunjung:", data[1])
                print("Santri:", data[2])
                print("Daerah:", data[3])
    
    elif pilihanmu == "3":
        print("Hapus data kunjungan")
        if len (data_kunjungan) == 0 :
            print ("Maaf belum ada data kunjungannya")
        else:
            hapus_id = int(input("Sialahakan masukkan ID yang ingin di hapus:"))
            for data in data_kunjungan:
                if data[0] == hapus_id:
                    data_kunjungan.remove(data)
                    print("data kunjungan", hapus_id, "berhasil dihapus")
                    break
                else:
                    print("Maaaf data tidak ditemukan")

    elif pilihanmu == "4":
        print("SELAMAT PROGRAM SISTEM KUNJUNGAN SANTRI PONDOK PESANTREN ANNUQAYAH TELAH SELESAI")
        break


