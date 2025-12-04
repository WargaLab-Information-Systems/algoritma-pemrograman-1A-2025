def cek_anagram(kata1, kata2):

    kata1_cek = sorted(kata1.lower())
    kata2_cek = sorted(kata2.lower())

    if kata1_cek == kata2_cek:
        print(f"'{kata1}' dan '{kata2}' adalah anagram.")
    else:
        print(f"'{kata1}' dan '{kata2}' bukan anagram.")

input_kata1 = input("Masukkan kata pertama: ")
input_kata2 = input("Masukkan kata kedua: ")

cek_anagram(input_kata1, input_kata2)