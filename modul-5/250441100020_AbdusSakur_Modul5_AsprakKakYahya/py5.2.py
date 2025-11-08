def anagram (kata1,kata2):
    return sorted(kata1.lower()) == sorted(kata2.lower())

kata1= input("masukan kata pertama: ")
kata2= input("masukan kata kedua: ")

if anagram (kata1,kata2):
    print("kedua kata anagram ")
else:
    print("kedua kata bukan anagram")