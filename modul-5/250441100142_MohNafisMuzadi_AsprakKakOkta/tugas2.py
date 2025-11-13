def cek(a, b):
    return sorted(a.lower()) == sorted(b.lower())

a = input("Masukkan kata pertama : ")
b = input("Masukkan kata kedua : ")


hasil = cek(a, b)
print(hasil)

if hasil :
    print("Kedua kata tersebut merupakan anagram")
else :
    print("Kedua kata tersebut bukan anagram")