
print("----------N0 2--------")

def cek_anagram(k1, k2):
    return sorted(k1) == sorted(k2)


kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

hasil = cek_anagram (kata1, kata2)
print("apakah diagram?  :", hasil)

if cek_anagram(kata1, kata2):
    print("Kedua kata tersebut adalah ANAGRAM ")
else:
    print("Kedua kata tersebut bukan ANAGRAM")
    















