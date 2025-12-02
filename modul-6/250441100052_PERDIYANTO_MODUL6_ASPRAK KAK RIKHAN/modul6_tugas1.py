data_utama = []
def data_kunjungan():
    id = int(input("masukan id kunjungan "))
    for i in data_utama:
        if i[0] == id:
            print("id sudah ada")
            return
    nama_pengunjung = input("masukan nama pengunjung ")
    nama_santri = input("masukan nama santri ")
    alamat = input("masukan alamat pengunjung (Jawa, Sumatra, Kalimantan) ")
    data_utama.append([id,nama_pengunjung,nama_santri,alamat]) 

def tampilkan():
    urutan = ["sumatra", "kalimantan","jawa"]
    for daerah in urutan:
        print(f"Data kunjungan dari daerah {daerah}")
        for i in data_utama:
            if i[3].lower() == daerah:
                print(f"\n id ke - {i[0]} \n nama pengunjung = {i[1]} \n nama santri = {i[2]} \n")

def hapus():
    urut = int(input("masukan id kunjungan yang ingin di hapus"))
    for i in data_utama:
        if i[0] == urut:
            data_utama.remove(i)
            print("berhasil")


while True:
    print("\n 1. tambah data kunjungan \n 2. liat data kunjungan \n 3. hapus data kunjugan \n 4. keluar")
    pilan = int(input("masukan nomor menu "))
    if pilan == 1:
        data_kunjungan()
    elif pilan == 2:
        tampilkan()
    elif pilan == 3:
        hapus()
    elif pilan == 4:
        break
    else:
        print("menu tidak sesuai")

