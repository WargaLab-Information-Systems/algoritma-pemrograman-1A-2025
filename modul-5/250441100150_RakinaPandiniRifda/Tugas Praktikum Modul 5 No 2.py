# Mengecek apakah dua kata adalah anagram
def cek_anagram(kata1, kata2):
    return sorted(kata1.lower()) == sorted(kata2.lower())

# Input
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

# Menggunakan fungsi untuk memeriksa anagram
hasil = cek_anagram(kata1, kata2)

# Output hasil
print("Hasil:", hasil)
print(f'"{kata1}" dan "{kata2}" {"adalah" if hasil else "bukan"} anagram.')