t1 = tuple(map(int, input("masukkan angka:").split()))
t2 = tuple(map(int, input("masukkan angka:").split()))
gabung = t1 + t2

hasil = []
for angka in gabung:
    if angka not in hasil:
        hasil.append(angka)
        
for i in range(len(hasil)): #  membandingkan 
    for j in range(i + 1, len(hasil)):
        if hasil[i] < hasil[j]:
            hasil[i], hasil[j] = hasil[j], hasil[i]  # Tukar posisi jika urutan salah
hasil_akhir = tuple(hasil)
print("Hasil akhir:", hasil_akhir)