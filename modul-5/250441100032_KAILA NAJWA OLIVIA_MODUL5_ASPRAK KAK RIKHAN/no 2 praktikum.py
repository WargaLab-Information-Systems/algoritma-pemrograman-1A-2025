#no 2
def cek_anagram(kata1, kata2):
    kata1 = kata1.lower()
    kata2 = kata2.lower()
    return sorted(kata1) == sorted(kata2)
    
# Input pengguna
kata1 = input("masukkan kata pertama: ")
kata2 = input("masukkan kata kedua: ")
hasil = cek_anagram (kata1, kata2)
print(f"apakah kata tersebut anagram?:{hasil}")

if hasil :
    print(f"kata tersebut merupakan anagram ")
else:
    print(f"kata tersebut bukan anagram ")

urut1 = sorted(kata1)
urut2 = sorted(kata2)
print(urut1)
print(urut2)