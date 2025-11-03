# SOAL NO 3
x = str("SOAL 3")
print(x)

kalimat = input("Masukkan sebuah kalimat: ")

vokal = "aiueo, AIUEO"
jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_kata = 0
jumlah_vokal_dalam_kata = 0


for huruf in kalimat:
    if (huruf >= 'A' and huruf <= 'Z') or (huruf >= 'a' and huruf <= 'z'):
        if huruf in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1


kata_sedang_dihitung = False
for huruf in kalimat:
    if huruf != " " and not kata_sedang_dihitung:
        jumlah_kata += 1
        kata_sedang_dihitung = True
    elif huruf == " ":
        kata_sedang_dihitung = False

kata = ""
for huruf in kalimat + " ":
    if huruf != " ":
        kata += huruf
    else :
        if kata != "" :
            jumlah_vokal_dalam_kata = 0
            for huruf in kata:
                if huruf in vokal:
                    jumlah_vokal_dalam_kata += 1
            print(f"Kata {kata} memiliki {jumlah_vokal_dalam_kata} huruf vokal.")
            kata = ""

print(f"Jumlah huruf vokal    : {jumlah_vokal}")
print(f"Jumlah huruf konsonan : {jumlah_konsonan}")
print(f"Jumlah kata           : {jumlah_kata}")


