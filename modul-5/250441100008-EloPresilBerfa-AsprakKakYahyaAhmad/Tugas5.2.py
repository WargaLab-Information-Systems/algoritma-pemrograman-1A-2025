def anagram(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    return sorted(str1) == sorted(str2)

a = input('Input Kata Pertama :')
b = input('Input Kata Kedua :')

if anagram(a,b):
    print(f"Kata {a} dan {b} adalah Anagram")
else:
    print(f"Kata {a} dan {b} bukan Anagram")
