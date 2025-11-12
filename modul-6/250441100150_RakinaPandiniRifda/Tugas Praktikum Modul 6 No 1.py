# Menampilkan sistem kunjungan santri
data_kunjungan = []
id_counter = 1
# create
def tambah_pengunjung(idc):
    ulang = True
    while ulang:
        try:
            n = ""
            while n == "":
                n_input = input("Nama pengunjung: ").lower()
                try:
                    float(n_input)
                    print("Input tidak valid! Nama pengunjung tidak boleh berupa angka. Coba lagi.")
                except ValueError:
                    if not n_input:
                        print("Nama pengunjung tidak boleh kosong!")
                    else:
                        n = n_input
            s = ""
            while s == "":
                s_input = input("Nama santri: ").lower()
                try:
                    float(s_input)
                    print("Input tidak valid! Nama santri tidak boleh berupa angka. Coba lagi.")
                except ValueError:
                    if not s_input:
                        print("Nama santri tidak boleh kosong!")
                    else:
                        s = s_input
            d = ""
            while d == "":
                d_input = input("Daerah (sumatra/kalimantan/jawa): ").lower()
                try:
                    float(d_input)
                    print("Input tidak valid! Daerah tidak boleh berupa angka. Coba lagi.")
                except ValueError:
                    if d_input not in ["sumatra", "kalimantan", "jawa"]:
                        print("Input salah! Pilih sumatra, kalimantan, atau jawa.")
                    else:
                        d = d_input

            # menyimpan data
            data_kunjungan.append([idc, n, s, d])
            print(f"Data ditambah (ID {idc})")
            idc += 1
            ulang = False
        except ValueError:
            print("Kesalahan input, coba lagi.")
    return idc
# read
def tampilkan_pengunjung():
    if not data_kunjungan:
        print("Belum ada data.")
        return
    for d in ["sumatra", "kalimantan", "jawa"]:
        print(f"--- {d} ---")
        f = [x for x in data_kunjungan if x[3] == d]
        if f:
            for x in f:
                print(f"ID:{x[0]} | Pengunjung:{x[1]} | Santri:{x[2]} | Asal:{x[3]}")
        else:
            print("(kosong)")
# delete
def hapus_pengunjung():
    if not data_kunjungan:
        print("Tidak ada data.")
        return
    while True:
        try:
            id_hapus = int(input("ID yang dihapus: "))
            for x in data_kunjungan:
                if x[0] == id_hapus:
                    data_kunjungan.remove(x)
                    print("Data dihapus.")
                    return
            print("ID tidak ditemukan.")
        except ValueError:
            print("Input salah! ID harus angka.")

menu_opsi = [("Tambah", tambah_pengunjung), ("Tampil", tampilkan_pengunjung), ("Hapus", hapus_pengunjung), ("Keluar", None)]

jalan = True
while jalan:
    print("=== Sistem Kunjungan Santri ===")
    for i in range(len(menu_opsi)):
        print(f"{i+1}. {menu_opsi[i][0]}")
    try:
        menu = int(input("Pilih menu (1-4): "))
        if 1 <= menu <= len(menu_opsi):
            nama, fungsi = menu_opsi[menu-1]
            if nama == "Keluar":
                print("Keluar program.")
                jalan = False
            elif fungsi == tambah_pengunjung:
                id_counter = fungsi(id_counter)
            else:
                fungsi()
        else:
            print("Pilihan tidak valid, coba lagi.")
    except ValueError:
        print("Input harus angka, coba lagi!")