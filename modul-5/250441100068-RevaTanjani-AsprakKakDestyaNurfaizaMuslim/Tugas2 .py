def cek_anagram(kata1, kata2):
    kata1 = kata1.lower()
    kata2 = kata2.lower()

    if len(kata1) != len(kata2):
        return False

    return True
k1 = input("Masukkan kata pertama: ")

k2 = input("Masukkan kata kedua: ")

if cek_anagram(k1, k2):
     print("True, kata tersebut adalah anagram\n")
else:
    print("False, kata tersebut bukan anagram\n")