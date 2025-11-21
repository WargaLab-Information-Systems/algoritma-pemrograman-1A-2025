def cek_anagram(kata1, kata2):
    return sorted(kata1.lower()) == sorted(kata2.lower())

k1 = input("Masukkan kata pertama: ")
k2 = input("Masukkan kata kedua: ")

if cek_anagram(k1, k2):
    print("Kedua kata adalah anagram.")
else:
    print("Bukan anagram.")