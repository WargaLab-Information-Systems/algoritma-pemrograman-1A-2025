# Fungsi untuk memeriksa apakah dua kata merupakan anagram
def anagram(kata1,kata2):
    kata1 = kata1 .lower()
    kata2 = kata2.lower()
    return sorted(kata1) == sorted(kata2) # Bandingkan hasil pengurutan huruf kedua kata
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")
hasil = anagram(kata1, kata2) # Cek apakah keduanya anagram

if hasil:
    print(f"{kata1} dan {kata2} : adalah anagram")
else:
    print(f"{kata1} dan {kata2} : bukan anagram")