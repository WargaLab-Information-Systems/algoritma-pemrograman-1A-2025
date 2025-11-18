def anagram(kata1, kata2):

    kata1 = kata1.lower()
    kata = kata2.lower()

    if sorted(kata1) == sorted(kata2):
        return True
    else:
        return False
kata1 = input("masukan kata pertama : ")
kata2 = input("masukan kata kedua : ")

if anagram(kata1, kata2):
    print(kata1, "dan", kata2, "adalah anagram")
else:
    print(kata1, "dan", kata2, "bukan anagram")
anagram(kata1, kata2)