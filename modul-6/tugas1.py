# def tambah_data(sumatra, kalimantan, jawa):
#     print("\nMasukkan data pengunjung:")

#     nama = input("Nama: ")
#     if not nama.replace(" ", "").isalpha(): 
#         print("nama harus huruf")
#         return
#     santri = input("Santri yang dijenguk: ")
#     asal = input("Asal daerah (Sumatra/Kalimantan/Jawa): ").lower()

#     # Pilih list berdasarkan asal
#     if asal == "sumatra":
#         data_list = sumatra
#     elif asal == "kalimantan":
#         data_list = kalimantan
#     elif asal == "jawa":
#         data_list = jawa
#     else:
#         print("Asal daerah tidak valid!")
#         return

#     # ID urut per daerah
#     id_counter = len(data_list) + 1

#     data_list.append([id_counter, nama, santri, asal.capitalize()])
#     print(f"Data berhasil ditambahkan ke ID {id_counter}!") 


# def hapus_data(sumatra, kalimantan, jawa):
#     print("\nPilih daerah untuk menghapus data:")
#     print("1. Sumatra")
#     print("2. Kalimantan")
#     print("3. Jawa")
#     d = input("Masukkan pilihan: ")

#     if d == "1":
#         data_list = sumatra
#         daerah = "Sumatra"
#     elif d == "2":
#         data_list = kalimantan
#         daerah = "Kalimantan"
#     elif d == "3":
#         data_list = jawa
#         daerah = "Jawa"
#     else:
#         print("Input salah!")
#         return

#     print(f"\nData di {daerah}:")
#     for data in data_list:
#         print(data)

#     try:
#         hapus_id = int(input("Masukkan ID yang ingin dihapus: "))
#     except ValueError:
#         print("Input tidak valid! Masukkan angka!")
#         return

#     for data in data_list:
#         if data[0] == hapus_id:
#             data_list.remove(data)
#             print(f"Data ID {hapus_id} berhasil dihapus!")
#             return

#     print("ID tidak ditemukan!")


# def tampilkan_data(sumatra, kalimantan, jawa):
#     print("\n>> Pengunjung Sumatra:")
#     for d in sumatra:
#         print(d)

#     print("\n>> Pengunjung Kalimantan:")
#     for d in kalimantan:
#         print(d)

#     print("\n>> Pengunjung Jawa:")
#     for d in jawa:
#         print(d)


# def main():
#     sumatra = []
#     kalimantan = []
#     jawa = []

#     while True:
#         print("\n===== MENU =====")
#         print("1. Tambah Data")
#         print("2. Hapus Data")
#         print("3. Tampilkan Semua Data")
#         print("4. Keluar")

#         pilihan = input("Pilih menu: ")

#         if pilihan == "1":
#             tambah_data(sumatra, kalimantan, jawa)

#         elif pilihan == "2":
#             hapus_data(sumatra, kalimantan, jawa)

#         elif pilihan == "3":
#             tampilkan_data(sumatra, kalimantan, jawa)

#         elif pilihan == "4":
#             print("Keluar program...")
#             break

#         else:
#             print("Input salah!")


# main()

def tambah_data(sumatra, kalimantan, jawa):
    print("\nMasukkan data pengunjung:")
    nama = input("Nama: ")
    santri = input("Santri yang dijenguk: ")
    asal = input("Asal daerah (Sumatra/Kalimantan/Jawa): ").strip().lower()

    # Menentukan list tujuan otomatis
    if asal == "sumatra":
        data_list = sumatra
        nomor = 1
    elif asal == "kalimantan":
        data_list = kalimantan
        nomor = 2
    elif asal == "jawa":
        data_list = jawa
        nomor = 3
    else:
        print("Asal daerah tidak valid!")
        return

    id_counter = len(data_list) + 1
    data_list.append([id_counter, nama, santri, asal.capitalize()])
    
    print(f"Data berhasil ditambahkan ke daerah {nomor} ({asal.capitalize()})!")


def hapus_data(sumatra, kalimantan, jawa):
    print("\nPilih daerah untuk menghapus data:")
    print("1. Sumatra")
    print("2. Kalimantan")
    print("3. Jawa")
    d = input("Masukkan pilihan: ")

    if d == "1":
        data_list = sumatra
    elif d == "2":
        data_list = kalimantan
    elif d == "3":
        data_list = jawa
    else:
        print("Input salah!")
        return

    print("\nData:")
    for data in data_list:
        print(data)

    try:
        hapus_id = int(input("Masukkan ID yang ingin dihapus: "))
    except:
        print("Input tidak valid!")
        return

    for data in data_list:
        if data[0] == hapus_id:
            data_list.remove(data)
            print("Data berhasil dihapus!")
            return

    print("ID tidak ditemukan!")


def tampilkan_data(sumatra, kalimantan, jawa):
    print("\n>> Pengunjung Sumatra:")
    for d in sumatra:
        print(d)
    
    print("\n>> Pengunjung Kalimantan:")
    for d in kalimantan:
        print(d)

    print("\n>> Pengunjung Jawa:")
    for d in jawa:
        print(d)
    

def main():
    sumatra = []
    kalimantan = []
    jawa = []

    while True:
        print("\n===== MENU =====")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Tampilkan Semua Data")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data(sumatra, kalimantan, jawa)

        elif pilihan == "2":
            hapus_data(sumatra, kalimantan, jawa)

        elif pilihan == "3":
            tampilkan_data(sumatra, kalimantan, jawa)

        elif pilihan == "4":
            print("Keluar program...")
            break

        else:
            print("Input salah!")


main()
