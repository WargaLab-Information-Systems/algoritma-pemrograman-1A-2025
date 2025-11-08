def cek_anagram(kata1, kata2):
    kata1 = kata1.lower()
    kata2 = kata2.lower()
    return sorted(kata1) == sorted(kata2)

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")
hasil = cek_anagram (kata1, kata2)
print(f"Apakah kata tersebut termasuk anagram?: {hasil}")

if hasil :
    print(f"Kata tersebut anagram.")
else:
    print(f"Kata tersebut tidak termasuk anagram. ")

urut1 = sorted(kata1)
urut2 = sorted(kata2)
print(urut1)
print(urut2)