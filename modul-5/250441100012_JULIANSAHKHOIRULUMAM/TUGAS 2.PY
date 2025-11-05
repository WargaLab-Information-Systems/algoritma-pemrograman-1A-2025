print("="*10," TUGAS 2 MODUL 5 ","="*10)

def anagram (kata1,kata2):
    if sorted (kata1.lower()) == sorted (kata2.lower()):
        return True
    else:
        return False

kata1 = input("Masukan Kata Pertama : ")
kata2 = input("Masukkkan Kata Kedua : ")
if anagram(kata1,kata2):
    print("Merupakan Anagram")
else:
    print("Bukan Anagram")
   
print(f"kata = {kata1} dengan kata {kata2} Merupakan {anagram(kata1,kata2)} Kata Anagram")
