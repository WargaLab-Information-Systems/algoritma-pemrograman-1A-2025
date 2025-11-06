def anagramaseli(kataku, katamu):
    kataku = kataku.replace(" ", "")
    katamu = katamu.replace(" ", "")

    return sorted(kataku) == sorted(katamu)

kataku = input("Masukkan kataku: ")
katamu = input("Masukkan katamu: ")

if anagramaseli (kataku, katamu):
    print(f"'{kataku}' dan '{katamu}' adalah anagram ")
else:
    print(f"'{kataku}' dan '{katamu}' bukanlah anagram ")
