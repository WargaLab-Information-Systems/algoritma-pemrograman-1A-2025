def anagram(kata_pertama, kata_kedua):
    if sorted(kata_pertama.lower()) == sorted(kata_kedua.lower()):
        return True
    else:
        return False
        
kata1 = input("masukan kata ke - 1 ")
kata2 = input("masukan angka ke - 2 ")
 
if anagram(kata1, kata2):
    print("Merupakan kata anagram")
else:
    print("bukan kata anagram")

print(f"kata = {kata1} dengan kata = {kata2} merupakan {anagram(kata1, kata2)} kata anagram")

