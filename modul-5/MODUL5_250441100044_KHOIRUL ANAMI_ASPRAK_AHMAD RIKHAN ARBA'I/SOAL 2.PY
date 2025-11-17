# SOAL 2
X = str("SOAL 2")
print(X)

def anagram(A, B):
    A = A.replace (" ", "").lower()
    B = B.replace (" ", "").lower()

    return sorted(A) == sorted(B)

while True:
    Kata_pertama = str(input("Silahkan masukkan kata pertama: "))
    kata_kedua = str(input("Silahkan masukkan kata ke dua: "))

    if anagram(Kata_pertama, kata_kedua):
        print(f"\nkata {Kata_pertama}, dan {kata_kedua}, merupakan ANAGRAM")
    else:
        print(f"kata {Kata_pertama}, dan {kata_kedua}, bukan ANAGRAM")

    ulang = input("Apakah anda ingin mengulangi lagi ?(YA/TIDAK)")
    if ulang.lower() != "iya":
        print (f"\nTerimakasih program telah selesai...")
        break

