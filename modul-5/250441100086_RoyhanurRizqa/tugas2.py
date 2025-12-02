def anagram(x,y):
    return sorted(x.lower()) == sorted(y.lower())

pertama = input("Masukkan kata pertama: ")
kedua = input("Masukkan kata kedua: ")

if anagram(pertama, kedua):
    print(f"{pertama} dan {kedua} adalah anagram!")
else:
    print(f"{pertama} dan {kedua} bukan anagram.")