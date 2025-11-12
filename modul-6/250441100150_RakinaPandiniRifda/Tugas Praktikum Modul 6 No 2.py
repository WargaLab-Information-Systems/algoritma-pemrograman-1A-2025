# Menampilkan gabungan kumpulan angka Mac Allister dan menggabungkannya menjadi satu data tanpa angka yang berulang
def input_tuple(pesan):
    angka = []
    while True:
        n = input(pesan)
        if n == "selesai":
            if angka: break
            print("Masukkan minimal satu angka sebelum mengetik 'selesai'!")
            continue
        try:
            angka.append(int(n))
        except:
            print("Input tidak valid! Masukkan angka atau ketik 'selesai' untuk berhenti.")
    return tuple(angka)

print("Masukkan angka untuk tuple pertama (ketik 'selesai' jika sudah):")
t1 = input_tuple("Angka: ")
print("Masukkan angka untuk tuple kedua (ketik 'selesai' jika sudah):")
t2 = input_tuple("Angka: ")

gabung = t1 + t2
unik = []
for n in gabung:
    if n not in unik: unik.append(n)

for i in range(len(unik)):
    for j in range(i + 1, len(unik)):
        if unik[i] < unik[j]:
            unik[i], unik[j] = unik[j], unik[i]

hasil = tuple(unik)
print("Hasil gabungan (urut dari besar ke kecil):", hasil)