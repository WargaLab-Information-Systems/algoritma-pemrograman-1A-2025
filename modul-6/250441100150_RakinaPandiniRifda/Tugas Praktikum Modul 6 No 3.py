# Menampilkan program tentang apakah deretan dapat dibagi menjadi dua bagian dengan jumlah yang sama
# program ini berbasis CRUD (Create, Read, Update, Delete)
data = []

def input_angka(pesan):
    a = None
    while a is None:
        try:
            a = int(input(pesan))
        except ValueError:
            print("Input harus berupa angka!")
    return a

def create(): data.append(input_angka("Masukkan angka baru: ")); print("Angka ditambahkan.")
def read(): print("Data kosong." if not data else f"Data saat ini: {data}")

def update():
    if not data: return print("Data kosong.")
    i = -1
    while i < 0 or i >= len(data):
        i = input_angka("Index yang ingin diubah: ")
        if 0 <= i < len(data):
            data[i] = input_angka("Angka baru: "); print("Data diubah."); break
        print("Index tidak ditemukan.")

def delete():
    if not data: return print("Data kosong.")
    i = -1
    while i < 0 or i >= len(data):
        i = input_angka("Index yang ingin dihapus: ")
        if 0 <= i < len(data):
            data.pop(i); print("Data dihapus."); break
        print("Index tidak ditemukan.")

def cek_pembagian():
    if not data: return print("Data kosong.")
    total = 0
    for x in data: total += x
    if total % 2: return print("False (jumlah ganjil)")
    kiri = 0
    for i in range(len(data)):
        kiri += data[i]
        if kiri * 2 == total: return print("True (dapat dibagi dua sama besar)")
    print("False (tidak dapat dibagi dua sama besar)")

print("=== Program Dominic Szoboszlai ===")
print("Menu: 1.Create  2.Read  3.Update  4.Delete  5.Cek  6.Keluar")

jalan = "ya"
while jalan == "ya":
    p = input("Pilih menu (1-6): ")
    if p == "1": create()
    elif p == "2": read()
    elif p == "3": update()
    elif p == "4": delete()
    elif p == "5": cek_pembagian()
    elif p == "6": print("Keluar program."); jalan = "tidak"
    else: print("Pilihan tidak valid, coba lagi.")