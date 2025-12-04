# Program menentukan apakah dua kata merupakan anagram

def cek_anagram(kata1,kata2):
    # Menghapus spasi dan ubah ke huruf kecil agar perbandingan adil
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()
    return sorted(kata1) == sorted(kata2)

# Program utama
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if cek_anagram(kata1,kata2):
    print(f"'{kata1}' dan '{kata2}' adalah anagram.")
else:
    print(f"'{kata1}' dan '{kata2}' bukan anagram.")

