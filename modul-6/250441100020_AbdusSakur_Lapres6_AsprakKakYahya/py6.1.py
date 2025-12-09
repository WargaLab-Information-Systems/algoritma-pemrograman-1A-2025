daftar = []
id = 1 

def tambah(daftar, id):
    nama = input("nama pengunjung: ")
    santri = input("nama santri: ")

    daerah = input("daerah (sumatra/kalimantan/jawa): ").lower()
    while daerah not in ["sumatra", "kalimantan", "jawa"]:
        daerah = input("daerah tidak valid, coba lagi: ").lower()

    daftar.append([nama, santri, daerah, id])
    print("data ditambahkan dengan ID", id)
    return id + 1

def tampil(daftar):
    if not daftar:
        print("belum ada data.")
        return

    urutan = ["sumatra", "kalimantan", "jawa"]

    for i in urutan:
        print("pengunjung dari", i + ":")
        ada = False
        for j in daftar:
            if j[2] == i:
                print(f"ID {j[3]}-{j[0]} menjenguk {j[1]}")
                ada = True
        if not ada:
            print("- Tidak ada -")

def hapus(daftar):
    try:
        target = int(input("masukan id yang mau dihapus: "))
        for i in range(len(daftar)):
            if daftar[i][3] == target:
                daftar.pop(i)
                print("data dihapus.")
                return
        print("id tidak ditemukan.")
    except:
        print("Masukkan angka yang benar.")


while True:
    print("1. tambah data")
    print("2. tampilkan data")
    print("3. hapus data")
    print("4. berhenti")

    p = input("masukan pilihan: ")

    if p == "1":
        id = tambah(daftar, id)
    elif p == "2":
        tampil(daftar)
    elif p == "3":
        hapus(daftar)
    elif p == "4":
        break
    else:
        print("pilihan tidak valid")