vokal = "aiueo"
konsonan = "bcdfghjklmnpqrstvwxyz"
teks = input("masukan teksnya : ")

total_vokal = 0
total_konsonan = 0
total_kata = 0
total_kalimat = 0

for huruf in teks:
    if huruf.isalpha():
        if huruf in vokal:
            total_vokal += 1
        else:
            total_konsonan += 1

kata = False
for huruf in teks:
    if huruf not in " ,.!?" and not kata:
        total_kata += 1
        kata = True
    elif huruf in " ,.!?":
        kata = False
    
    if huruf in ".!?":
        total_kalimat += 1

print("jumlah katanya adalah : ", total_kata)
print("jumlah kalimatnya adalah :  ", total_kalimat)
print("jumlah huruf vokalnya adalah : ", total_vokal)
print("jumlah huruf konsonannya adalah : ", total_konsonan)